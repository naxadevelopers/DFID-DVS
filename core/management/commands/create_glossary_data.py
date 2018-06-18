import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import GlossaryData, Indicator


class Command(BaseCommand):
    help = 'load indicators from province_indicators_filtered file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3])
        indicator_list = df['Indicators'].unique()

        for indicator in indicator_list:
            new_glossary_data, created = GlossaryData.objects.get_or_create(title=Indicator.objects.get(name=indicator))
            if created:
                self.stdout.write('Successfully created Glossary data.. "%s"' % new_glossary_data)