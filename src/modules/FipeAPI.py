import requests
import json
from datetime import date
from dateutil.relativedelta import relativedelta
from time import sleep
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from playwright.sync_api import sync_playwright


class FipeAPI:
    def __init__(self, vehicle_id:int, ref_table_id:int) -> None:
        self.url = 'https://veiculos.fipe.org.br/api/veiculos'
        self.vehicle_id = vehicle_id
        self.ref_table_id = ref_table_id
        self.ref_table_date = self.date_from_ref_table_id()
        self.headers = {
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'Connection': 'keep-alive',
            'referer': 'https://veiculos.fipe.org.br/',
            'origin': 'https://veiculos.fipe.org.br',

        }

    def date_from_ref_table_id(self):
        delta = lambda id: id - 281 if id != 281 else 0
        ref_table_date = date(2022, 1, 1) + relativedelta(months=delta(self.ref_table_id))
        return ref_table_date
    
    def query_brands(self):
        query_url = '/ConsultarMarcas'

        payload = {
            'codigoTabelaReferencia': str(self.ref_table_id),
            'codigoTipoVeiculo': str(self.vehicle_id),
        }

        response = requests.post(
            self.url + query_url,
            headers=self.headers,
            data=payload
            )
        
        sleeps = 0
        while response.status_code != 200:
            sleeps += 1
            print(f'Waiting response [brands]...{sleeps}')
            sleep(sleeps * 60)
        else:
            return response.json()
    
    def query_brands_to_sql(self):
        with open('./sql/02-brands.sql', 'w') as file:
            file.write('\c fipe_database;\n\n')

            insert_all_values = ''

            for brand in self.query_brands():
                insert_values = f"('{self.ref_table_date}', {brand['Value']}, '{brand['Label']}'),\n"
                insert_all_values += insert_values
            
            file.write(f'''INSERT INTO fipe.brands(table_date, brand_id, brand_name)\nVALUES\n{insert_all_values[0:-2]};''')

    def query_models(self, brand_id:int):
        session = requests.Session()
        session.headers.update(self.headers)

        query_url = '/ConsultarModelos'

        payload = {
            'codigoTipoVeiculo': str(self.vehicle_id),
            'codigoTabelaReferencia': str(self.ref_table_id),
            'codigoMarca': str(brand_id),
            }

        response = session.post(
            self.url + query_url,
            data=payload
            )

        sleeps = 0
        while response.status_code != 200:
            self.update_headers()
            session.headers.update(self.headers)
            sleeps += 1
            print(f'Waiting response [models]...{sleeps}')
            sleep(sleeps)
        else:
            return response.json()
    
    def query_model_to_sql(self):
        with open('./sql/03-models.sql', 'w') as file:
            file.write('\c fipe_database;\n\n')

            for brand in self.query_brands():
                for model in self.query_models(brand_id=brand['Value'])['Modelos']:
                    values = f"({model['Value']}, '{model['Label']}', {brand['Value']})"
                    file.write(f'''INSERT INTO fipe.models(model_id, model_name, brand_id)
                    VALUES {values};\n\n''')
                    print(values)

    def update_headers(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            captured_headers = {}

            def on_request(req):
                try:
                    if req.is_navigation_request():
                        # req.headers() retorna um dict com os headers do request
                        captured_headers.update(req.headers)
                except Exception:
                    pass

            page.on("request", on_request)

            page.goto("https://www.fipe.org.br", timeout=60000)
            # aguarde se precisar: page.wait_for_load_state("networkidle")

            print("Headers capturados (exemplo):")
            for k, v in captured_headers.items():
                print(f"{k}: {v}")

            # pegar cookies do contexto (lista de dicts)
            cookies = page.context.cookies()
            print("\nCookies capturados:")
            for c in cookies:
                print(f"{c['name']} = {c['value']} (domain: {c.get('domain')})")

            browser.close()

            self.headers = captured_headers



#     def query_value_with_all_parameters(
#             self,
#             vehicle_id,
#             bra

#             ):
#         '''

#         '''
#         url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'
#         payload = {

#         }

# data = {
#     'codigoTipoVeiculo': '1',
#     'codigoTabelaReferencia': '310',
#     'codigoMarca': '22',
#     'codigoModelo': '4514',
#     'anoModelo': '2012',
#     'codigoTipoCombustivel': '1',
#     'tipoVeiculo': 'carro',
#     'modeloCodigoExterno': '',
#     'tipoConsulta': 'tradicional',
# }

# response = requests.post(
#     'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros',
#     data=data,
# )

# print(response.json())