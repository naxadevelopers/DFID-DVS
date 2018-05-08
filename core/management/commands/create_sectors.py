import sys
import argparse

import pandas as pd

from django.core.management.base import BaseCommand

from core.models import Sector


class Command(BaseCommand):
    help = 'Create default Sectors from sectors file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType())

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3])
        sector = [
            Sector(
                    name=df['Sector'][row],
                    code=df['Sector Code'][row],

            ) for row in range(0, 13)
        ]
        sector = Sector.objects.bulk_create(sector)
        if sector:
            self.stdout.write('Successfully Sectors ..')

