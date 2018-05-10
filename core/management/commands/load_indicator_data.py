import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Indicator, IndicatorData, Province


class Command(BaseCommand):
    help = 'load indicator data from province_indicators_filtered file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3]).fillna(value=0)
        indicator_data = [
            IndicatorData(
                    province=Province.objects.get(name=df['Province'][row]),
                    indicator=Indicator.objects.get(name=df['Indicators'][row]),
                    value=df['Value'][row],
                    unit=df['Unit'][row],
                    years=df['Years'][row],
                    source=df['Source'][row],
            ) for row in range(0, 147)
        ]
        indicator_data = IndicatorData.objects.bulk_create(indicator_data)
        if indicator_data:
            self.stdout.write('Successfully loaded Indicator data..')
