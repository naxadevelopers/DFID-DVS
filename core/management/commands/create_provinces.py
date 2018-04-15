from django.core.management.base import BaseCommand
from core.models import Province


class Command(BaseCommand):
    help = 'Create default provinces'

    def handle(self, *args, **options):
        provinces_list = [1, 2, 3, 4, 5, 6, 7]
        for province in provinces_list:
            new_province, created = Province.objects.get_or_create(name=province)
            if created:
                self.stdout.write('Successfully created Provinces .. "%s"' % province)