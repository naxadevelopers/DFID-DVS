import sys
import argparse

import pandas as pd

from django.core.management.base import BaseCommand

from core.models import Area, Poverty


class Command(BaseCommand):
    help = 'Create poverty data from final_lgu_pov_slim.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType())

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        poverty_data = [
            Poverty(
                    lgu=df['lgu'][row],
					hlcit_code=Area.objects.get(hlcit_code=df['hlcit_code'][row]),
					lu_type=df['lu_type'][row],
					lgu_FGT_0=df['lgu_FGT_0'][row],
					lgu_FGT_1=df['lgu_FGT_1'][row],
					lgu_FGT_2=df['lgu_FGT_2'][row],
					female_lit_rate=df['female_lit_rate'][row],
					male_lit_rate=df['male_lit_rate'][row],
					total_lit_rate=df['total_lit_rate'][row]

            ) for row in range(0, 753)
        ]
        poverty_data = Poverty.objects.bulk_create(poverty_data)
        if poverty_data:
            self.stdout.write('Successfully loaded poverty data ..')