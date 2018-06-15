import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Area


class Command(BaseCommand):
    help = 'load area data from munis.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        area_data = [
            Area(
                hlcit_code=df['HLCIT_CODE'][row],
                type=df['TYPE_EN'][row],
                local_name=df['LU_Name'][row]

        ) for row in range(0, 775)
        ]
        area_data = Area.objects.bulk_create(area_data)
        if area_data:
            self.stdout.write('Successfully loaded Area data ..')