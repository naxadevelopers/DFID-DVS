from rest_framework import serializers

from .models import ProvinceData, Province, District, Sector, Partner, Program


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        exclude = ()


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        exclude = ()


class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        exclude = ()


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        exclude = ()


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        exclude = ()

class ProvinceDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProvinceData
        fields = '__all__'


