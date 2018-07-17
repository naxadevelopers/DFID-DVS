from django.core.management.base import BaseCommand

from core.models import Partner


# test data for partners
class Command(BaseCommand):
    help = 'Create default Partners'

    def handle(self, *args, **options):
        partner_list = ["Partner 1",
                        "Partner 2",
                        "Partner 3",
                        "Partner 4",
                        "Partner 5",
                        "Partner 6",
                        "Partner 7",

                        ]
        for partner in partner_list:
            new_partner, created = Partner.objects.get_or_create(name=partner)
            if created:
                self.stdout.write('Successfully created partners .. "%s"' % partner)