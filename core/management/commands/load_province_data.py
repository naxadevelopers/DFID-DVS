import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Province, ProvinceData


class Command(BaseCommand):
    help = 'load province data from province.xlsx file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3])
        try:
            provinces = [
                ProvinceData(
                        province=Province.objects.get(name='Province '+str(row)),
                        total_population=df.ix[row]['Indicator 1'],
                        area=float(df.ix[row]['Unnamed: 1']),
                        population_density=int(df.ix[row]['Indicator 2']),
                        poverty_rate=df.ix[row]['Indicator 3'],
                        population_under_poverty_line=int(df.ix[row]['Indicator 4']),
                        per_capita_income=df.ix[row]['Indicator 5'],
                        hh_by_lowest_wealth_quantiles=df.ix[row]['Indicator 6'],
                        gdp=int(df.ix[row]['Indicator 10']),
                        human_development_index=df.ix[row]['Indicator 7'],
                        minute_access_to=df.ix[row]['Indicator 8'],
                        vulnerability_index=df.ix[row]['Indicator 9'],

                ) for row in range(1, 8)
            ]
            provinces_data = ProvinceData.objects.bulk_create(provinces)
            if provinces_data:
                self.stdout.write('Successfully loaded Provinces data ..')

        except Province.DoesNotExist:
            pass