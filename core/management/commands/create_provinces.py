from django.core.management.base import BaseCommand

from core.models import Province, District


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
            {"Province 1": ["Bhojpur", "Dhankuta", "Ilam", "Jhapa", "Khotang", "Morang", "Okhaldhunga", "Panchthar",
                            "Sankhuwasabha", "Solukhumbu", "Sunsari", "TapleJung", "Terhathun", "Udayapur"]},
            {"Province 2": ["Bara", "Dhanusa", "Mahottari", "Parsa", "Rautahat", "Saptari", "Sarlahi", "Siraha"]},
            {"Province 3": ["Bhaktapur", "Chitwan", "Dhading", "Dolakha", "Kathmandu", "Kavrepalanchowk", "Lalitpur",
                            "Makwanpur", "Nuwakot", "Ramechhap", "Rasuwa", "Sindhuli", "Sindhupalchowk"]},
            {"Province 4": ["Baglung", "Gorkha", "Kaski", "Lamjung", "Manang", "Mustang", "Myagdi", "Nawalparasi",
                            "Parbat", "Syangja", "Tanahun"]},
            {"Province 5": ["Arghakhanchi", "Banke", "Bardiya", "Dang", "Gulmi", "Kapilbastu", "Palpa", "Pyuthan",
                            "Rolpa", "Rukam", "Rupandehi"]},
            {"Province 6": ["Dailekh", "Dolpa", "Humla", "Jajarkot", "Jumla", "Kalikot", "Mugu", "Salyan", "Surkhet"]},
            {"Province 7": ["Achham", "Baitadi", "Bajhang", "Bajura", "Dadeldhura", "Darchula", "Doti", "Kailali",
                            "Kanchanpur"]},


            ]

        for province_district in district_list:
            for province, district in province_district.items():
                new_province, created = District.objects.get_or_create(province=Province.objects.get(name=province),
                                                                       name=district)
                if created:
                    self.stdout.write('Successfully created Province district .."%s","%s"' % (province, district))