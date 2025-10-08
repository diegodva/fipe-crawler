import requests

cookies = {
    'ROUTEID': '.13',
    '_gid': 'GA1.3.191791656.1719277876',
    '_gcl_au': '1.1.1796672173.1719277899',
    'cf_clearance': 'hbPsgMs_s7mY8eWMNKDcH2AObXsjAuTwY47LRCOwD28-1719277720-1.0.1.1-4SKpobnQ0u1ZXEEme1SQZerm8q820_Qawupydxc2MnTY3Frtaxjkexlb...7AOsXU3owGF_EmJOZq91AZ.NPYw',
    'ASP.NET_SessionId': 'tx1nnfjoi4ivhxvvhaoejwce',
    '__RequestVerificationToken': '9RvR-t6127R42KucgbA7hRMzItQXzlJyITIzoNeYgNocWp9b2bXOW0C6oxuG_w0nKXnl-jwzdM6D667l8D6Bjm7JK1GqgETioPqlclDiaoo1',
    '_ga': 'GA1.3.937490961.1712539631',
    '_gat': '1',
    '_ga_WN7SEBCDBR': 'GS1.3.1719375790.5.1.1719376526.56.0.0',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ROUTEID=.13; _gid=GA1.3.191791656.1719277876; _gcl_au=1.1.1796672173.1719277899; cf_clearance=hbPsgMs_s7mY8eWMNKDcH2AObXsjAuTwY47LRCOwD28-1719277720-1.0.1.1-4SKpobnQ0u1ZXEEme1SQZerm8q820_Qawupydxc2MnTY3Frtaxjkexlb...7AOsXU3owGF_EmJOZq91AZ.NPYw; ASP.NET_SessionId=tx1nnfjoi4ivhxvvhaoejwce; __RequestVerificationToken=9RvR-t6127R42KucgbA7hRMzItQXzlJyITIzoNeYgNocWp9b2bXOW0C6oxuG_w0nKXnl-jwzdM6D667l8D6Bjm7JK1GqgETioPqlclDiaoo1; _ga=GA1.3.937490961.1712539631; _gat=1; _ga_WN7SEBCDBR=GS1.3.1719375790.5.1.1719376526.56.0.0',
    'origin': 'https://veiculos.fipe.org.br',
    'priority': 'u=0, i',
    'referer': 'https://veiculos.fipe.org.br/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'codigoTipoVeiculo': '1',
    'codigoTabelaReferencia': '310',
    # 'codigoModelo': '',
    'codigoMarca': '21',
    # 'ano': '',
    # 'codigoTipoCombustivel': '',
    # 'anoModelo': '',
    # 'modeloCodigoExterno': '',
}

response = requests.post('https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos',
                        #   cookies=cookies,
                        #     headers=headers,
                              data=data)

print(response.json())