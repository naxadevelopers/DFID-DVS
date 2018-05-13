from django.core.management.base import BaseCommand

from core.models import Layer, Sector


class Command(BaseCommand):
    help = 'Create default layer'

    def handle(self, *args, **options):

        layer_sector_list = [
            {"Financial institutions": ["EI"]},
            {"Health Facilities": ["HE"]},
            {"Landslide hazard from rainfall": ["NSA"]},
            {"Landslide hazard from EQ": ["NSA"]},
            {"2015 Population Estimates": ["NSA"]},
            {"Admin 1 (Province) Boundaries": ["NSA"]},
            {"Admin 2 (local government) boundaries": ["NSA"]},
            {"Admin 3 (ward) boundaries": ["NSA"]},
            {"OLD Admin 2 (district) boundaries": ["NSA"]},
            {"OLD Admin 3 (VDC) boundaries": ["NSA"]},
            {"OLD Admin 4 (ward) boundaries": ["NSA"]},
            {"Schools": ["ED"]},
            {"National Parks": ["NSA"]},
            {"Dams": ["EI", "EP", "WSS"]},
            {"Hydropower stations": ["EI", "EP", "WSS"]},
            {"Market centers (EQ districts)": ["EI", "EP"]},
            {"Roads": ["NSA"]},
            {"Travel times to schools": ["ED"]},
            {"Travel times to medical facilities": ["HE"]},
            {"Travel times to markets": ["EI"]},
            {"Travel times to financial institutions": ["EI"]},
            {"Landcover": ["NSA"]},
            {"Bridges": ["NSA"]},
            {"Terrain (hillshade)": ["NSA"]},


        ]

        for layer_sector in layer_sector_list:
            for layer, sector_list in layer_sector.items():
                layer_data_obj = Layer.objects.create(name=layer)

                for sector in sector_list:
                    sector_obj = Sector.objects.get(code=sector)
                    layer_data_obj.sector.add(sector_obj)
                layer_data_obj.save()
                if layer_data_obj:
                    self.stdout.write('Successfully created layer"s sectors "%s","%s"' % (layer, sector_list))
