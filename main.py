import pandas as pd
from src.modules.FipeAPI import FipeAPI
from datetime import date
from dateutil.relativedelta import relativedelta


def main():
    fipe_api = FipeAPI(vehicle_id=1, ref_table_id=326)
    # fipe_api.query_brands()
    fipe_api.query_brands_to_sql()
    # print(fipe_api.query_models(brand_id=21).text)
    fipe_api.query_model_to_sql()

main()

# fipe_api = FipeAPI(vehicle_id=1, ref_table_id=310)

# for brand in fipe_api.query_brands()[0:2]:
#     for model in fipe_api.query_models(brand_id=brand['Value']):
#         print(model)

# print(fipe_api.query_brands())
# # print(fipe_api.query_models(brand_id=21))
