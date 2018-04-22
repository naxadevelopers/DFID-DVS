from django.core.management.base import BaseCommand
from core.models import Province, ProvinceData

import pandas as pd


class Command(BaseCommand):
    help = 'load province data'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    # def handle(self, *args, **options):
    #     df = pd.read_excel('core/province.xlsx')
    #     try:
    #         provinces = [
    #             ProvinceData(
    #                     province=Province.objects.get(name=row),
    #                     total_population=df.ix[row]['Indicator 1'],
    #                     area=float(df.ix[row]['Unnamed: 1']),
    #                     population_desnity=int(df.ix[row]['Indicator 2']),
    #                     poverty_rate=df.ix[row]['Indicator 3'],
    #                     population_under_poverty_line=int(df.ix[row]['Indicator 4']),
    #                     per_capita_income=df.ix[row]['Indicator 5'],
    #                     hh_by_lowest_wealth_quantiles=df.ix[row]['Indicator 6'],
    #                     gdp=int(df.ix[row]['Indicator 10']),
    #                     human_development_index=df.ix[row]['Indicator 7'],
    #                     minute_access_to=df.ix[row]['Indicator 8'],
    #                     vulnerability_index=df.ix[row]['Indicator 9'],
    #
    #             ) for row in range(1, 8)
    #         ]
    #         ProvinceData.objects.bulk_create(provinces)
    #     except Province.DoesNotExist:
    #         pass