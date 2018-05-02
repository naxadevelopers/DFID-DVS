from rest_framework import serializers
from rest_framework.serializers import CharField, IntegerField

from .models import ProvinceData, Province, District, Sector, Partner, Program, DistrictSpending


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        exclude = ()


class DistrictSerializer(serializers.ModelSerializer):
    province = CharField(source='province.name', read_only=True)

    class Meta:
        model = District
        fields = ('id', 'name', 'province')


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
    province = CharField(source='province.name', read_only=True)
    district = IntegerField(source='province.districts.count', read_only=True)

    class Meta:
        model = ProvinceData
        fields = ('id', 'province',  'district', 'total_population', 'area', 'population_density', 'poverty_rate',
                  'population_under_poverty_line', 'per_capita_income', 'hh_by_lowest_wealth_quantiles',
                  'human_development_index', 'minute_access_to', 'vulnerability_index', 'gdp'
                  )


class DistrictSpendingSerializer(serializers.ModelSerializer):
    district = CharField(source='district.name')
    district_id = IntegerField(source='district.id')
    program = CharField(source='program.name')
    program_id = IntegerField(source='program.id')

    class Meta:
        model = DistrictSpending
        fields = ('id', 'district', 'district_id', 'program', 'program_id', 'annual_spend')