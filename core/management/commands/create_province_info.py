from django.core.management.base import BaseCommand

from core.models import Province, ProvinceInfo


class Command(BaseCommand):
    help = 'Create default province info'

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
            new_province_info, created = ProvinceInfo.objects.get_or_create(name=Province.objects.get(name=province))
            if created:
                self.stdout.write('Successfully created Province Info .. "%s"' % new_province_info)