import sys
import argparse

from django.core.management.base import BaseCommand
import pandas as pd

from core.models import DistrictSpending, District, Program


class Command(BaseCommand):
    help = 'load district spending data from district_spending.xls file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3], sheet_name="Programme 1").fillna(value=0)
        for dist in range(5, 82):
            for col in range(2, 10):
                district_spending = [
                    DistrictSpending(
                            district=District.objects.get(name=df.ix[dist]['Programe Name']),
                            program=Program.objects.get(name=df.columns[col]),
                            annual_spend=float(df.ix[dist][col]),

                    )
                ]
                district_spending_data = DistrictSpending.objects.bulk_create(district_spending)
                if district_spending_data:
                    self.stdout.write('Successfully loaded district spending data ..')