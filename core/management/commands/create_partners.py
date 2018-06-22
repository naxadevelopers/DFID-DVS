from django.core.management.base import BaseCommand

from core.models import Program


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
                        "PArtner 7",

                        ]
        for partner in partner_list:
            new_partner, created = Program.objects.get_or_create(name=partner)
            if created:
                self.stdout.write('Successfully created partnermes .. "%s"' % partner)