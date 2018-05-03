import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Indicator


class Command(BaseCommand):
    help = 'load Indicators from federalism_draft file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3], sheet_name="Province").replace({r'\n': ' '}, regex=True)
        indicators = df['Indicators'].unique()
        for indicator in indicators:
            new_indicator, created = Indicator.objects.get_or_create(name=indicator)
            if created:
                self.stdout.write('Successfully created Indicators .. "%s"' % new_indicator)