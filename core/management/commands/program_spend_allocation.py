import sys
import argparse

import pandas as pd

from django.core.management.base import BaseCommand

from core.models import ProgramSpendAllocation, Program, Area


class Command(BaseCommand):
    help = 'Create Program Spend Allocation from xlsx file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType())

    def handle(self, *args, **options):
        df = pd.read_excel(sys.argv[3]).fillna(value='')
        for row in range(0, 752):
            if df['Sakchyam partnership (first tier through CF)'][row] == 'Yes':
                ProgramSpendAllocation.objects.create(
                    program=Program.objects.get(name="Access to Finance Programme"),
                    district=df['District'][row],
                    hlcit_code=Area.objects.get(hlcit_code=df['HLCIT_CODE'][row]),
                    local_unit=df['Local Unit'][row],
                    partnership=df['Sakchyam partnership (first tier through CF)'][row],
                    spend_allocation_npr=df['Tentative spend allocation (NPR)'][row],
                    spend_allocation_gbp=df['Tentative spend allocation (GBP)'][row],

                )

            self.stdout.write('Successfully Created program spend data ..')

