from django.core.management.base import BaseCommand
from core.models import Province


class Command(BaseCommand):
    help = 'Create default provinces'

    def handle(self, *args, **options):
        provinces_list = ["Province 1",
                          "Province 2",
                          "Province 3",
                          "Province 4",
                          "Province 5",
                          "Province 6",
                          "Province 7",
                          ]
        for province in provinces_list:
            new_province, created = Province.objects.get_or_create(name=province)
            if created:
                self.stdout.write('Successfully created Provinces .. "%s"' % province)

        district_list = [
            {"Province 1":["Jhapa", "Ilam", "TapleJung"]},
                          ]
        for province_district in district_list:
            for district in province_district:
                new_province, created = District.objects.get_or_create(name=province)
                if created:
                    self.stdout.write('Successfully created Provinces .. "%s"' % province)