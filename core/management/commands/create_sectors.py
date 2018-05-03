from django.core.management.base import BaseCommand

from core.models import Sector


class Command(BaseCommand):
    help = 'Create default Sectors'

    def handle(self, *args, **options):
        sector_list = ["Health Sector",
                       "Education Sector",
                       "Agriculture Sector",
                       "Energy Sector",
                       "Finance Sector",
                       "Industry Sector",
                        ]
        for sector in sector_list:
            new_sector, created = Sector.objects.get_or_create(name=sector)
            if created:
                self.stdout.write('Successfully created Sector.. "%s"' % sector)