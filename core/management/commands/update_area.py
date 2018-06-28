import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Area, Province


class Command(BaseCommand):
    help = 'update area data from munis.csv file for adding province in each municipality'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        for i in range(0, 775):
            Area.objects.filter(hlcit_code=df['HLCIT_CODE'][i]).update(province=Province.objects.get(name='Province ' + str(df['STATE'][i])))
