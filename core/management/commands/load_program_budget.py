import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Program, ProgramBudget


class Command(BaseCommand):
    help = 'load program budget from nepal_data_mapping file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3], sheet_name="Programmes")
        try:
            program_budget = [
                ProgramBudget(
                        program=Program.objects.get(name=df['Programme'][row]),
                        code=df['Prog Code'][row],
                        budget=df['Value'][row]
                ) for row in range(0, 23)
            ]
            program_budget = ProgramBudget.objects.bulk_create(program_budget)
            if program_budget:
                self.stdout.write('Successfully loaded Program budget data ..')

        except Program.DoesNotExist:
            pass