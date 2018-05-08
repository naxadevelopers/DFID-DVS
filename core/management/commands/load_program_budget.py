import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Program, ProgramBudget


class Command(BaseCommand):
    help = 'load program budget from programs file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType())

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3])
        try:
            budget = [
                ProgramBudget(
                        program=Program.objects.get(name=df['Program'][row]),
                        budget=df['Value'][row]


            ) for row in range(0, 8)
            ]
            budget = ProgramBudget.objects.bulk_create(budget)
            if budget:
                self.stdout.write('Successfully loaded Program budget data ..')

        except Program.DoesNotExist:
            pass