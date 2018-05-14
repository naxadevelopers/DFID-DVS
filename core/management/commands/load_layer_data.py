import sys
import argparse

import pandas as pd

from django.core.management.base import BaseCommand

from core.models import Layer, LayerData


class Command(BaseCommand):
    help = 'Create layer data from Spatial Data List file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType())

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3]).fillna(value=0)
        layer_data = [
            LayerData(
                    layer_name=Layer.objects.get(name=df['Dataset'][row]),
                    source=df['Source'][row],
                    date=df['Date'][row],
                    type=df['Type'][row],
                    notes=df['Notes'][row],

            ) for row in range(0, 24)
        ]
        layer_data = LayerData.objects.bulk_create(layer_data)
        if layer_data:
            self.stdout.write('Successfully loaded layer data ..')

