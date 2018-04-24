from django.core.management.base import BaseCommand

from core.models import Program


class Command(BaseCommand):
    help = 'Create default Programmes'

    def handle(self, *args, **options):
        program_list = ["Nepal Climate Change Support Programme",
                        "Post-Earthquake Reconstruction Programme",
                        "Nepal Local Governance Programme",
                        "Nepal Health Sector Programme",
                        "IP-SSJ",
                        "Sakchyam Access to Finance",
                        "AiiN",
                        "RAP3",
                        ]
        for program in program_list:
            new_program, created = Program.objects.get_or_create(name=program)
            if created:
                self.stdout.write('Successfully created programmes .. "%s"' % program)