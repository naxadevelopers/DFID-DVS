from django.core.management.base import BaseCommand

from core.models import Program


class Command(BaseCommand):
    help = 'Create default Programmes'

    def handle(self, *args, **options):
        program_list = ["Nepal Climate Change Support Programme",
                        "Nepal Local Governance Support Programme",
                        "Rural Access Programme 3",
                        "Climate Smart Development for Nepal",
                        "Nepal Health Sector Programme",
                        "Post-Earthquake Reconstruction Programme",
                        "Strengthening disaster resilience in Nepal",
                        "Integrated Programme for Strengthening Security and Justice",
                        "Access to Finance Programme",
                        "Accelerating Investment and Infrastructure in Nepal",
                        "Skills for Employment Programme",
                        "Nepal Peace Support Programme",
                        "Support for the Economic Empowerment of Women and Girls",
                        "Rural Water and Sanitation Programme Phase V",
                        "Samarth-Nepal Market Development Programme",
                        "Family Planning Project",
                        "Evidence for Development",
                        "Strengthening Road Safety in Nepal",
                        "Improving Public Financial Management and Accountability in Nepal",
                        "Operational Support for Housing Reconstruction in Nepal",
                        "UK Contribution to the Government of Nepal’s Post-Earthquake Housing Reconstruction Grant Programme",
                        "Seismic Retrofitting of Unsafe Housing in Nepal",
                        "Emergency Support to Vulnerable Households",
                        "Risk Management Office (RMO)-Phase III"
                        ]
        for program in program_list:
            new_program, created = Program.objects.get_or_create(name=program)
            if created:
                self.stdout.write('Successfully created programmes .. "%s"' % program)