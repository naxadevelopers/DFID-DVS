import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Indicator, FederalismDraft, Province


class Command(BaseCommand):
    help = 'load federalism draft'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3], sheet_name="Province").fillna(value=0).replace({r'\n': ' '}, regex=True)
        federalism_draft = [
            FederalismDraft(
                    indicator=Indicator.objects.get(name=df['Indicators'][row]),
                    dfid_qn=df['DFID Q.N.'][row],
                    province=Province.objects.get(name=df['Province'][row]),
                    values=df['Values'][row],
                    unit=df['Unit'][row]
            ) for row in range(0, 455)
        ]
        federalism_draft = FederalismDraft.objects.bulk_create(federalism_draft)
        if federalism_draft:
            self.stdout.write('Successfully loaded Federalism draft data..')
