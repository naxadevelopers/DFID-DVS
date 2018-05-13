import sys
import argparse

import pandas as pd

from django.core.management.base import BaseCommand

from core.models import Sector, SectorData, Program


class Command(BaseCommand):
    help = 'Create Sectors data from programs file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType())

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3])
        sector_data = [
            SectorData(
                    sector=Sector.objects.get(code=df['Sector Code'][row]),
                    program=Program.objects.get(name=df['Program'][row])

            ) for row in range(0, 8)
        ]
        sector_data = SectorData.objects.bulk_create(sector_data)
        if sector_data:
            self.stdout.write('Successfully loaded Sectors data ..')

