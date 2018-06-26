from rest_framework import serializers
from rest_framework.serializers import CharField, IntegerField, FloatField

from .models import ProvinceData, Province, District, Sector, Partner, Program, DistrictSpending, Indicator, \
    IndicatorData, ProvinceInfo, ProgramData, CountryData, LayerData, Dataset, Area, GlossaryData, Pdf


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        exclude = ()


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('id', 'name')


class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        exclude = ()


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('id', 'name', 'description')


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'sectors')


class ProvinceDataSerializer(serializers.ModelSerializer):
    province = CharField(source='province.name', read_only=True)
    total_budget = FloatField(source='budget')

    class Meta:
        model = ProvinceData
        fields = ('id', 'province',  'district', 'total_population', 'area', 'population_density', 'poverty_rate',
                  'population_under_poverty_line', 'per_capita_income', 'hh_by_lowest_wealth_quantiles',
                  'human_development_index', 'minute_access_to', 'vulnerability_index', 'gdp', 'active_programmes',
                  'total_budget', 'description'
                  )


class DistrictSpendingSerializer(serializers.ModelSerializer):
    district = CharField(source='district.name')
    district_id = IntegerField(source='district.id')
    program = CharField(source='program.name')
    program_id = IntegerField(source='program.id')

    class Meta:
        model = DistrictSpending
        fields = ('id', 'district', 'district_id', 'program', 'program_id', 'annual_spend')


class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ()


class IndicatorDataSerializer(serializers.ModelSerializer):
    province = CharField(source='province.name', read_only=True)
    province_id = IntegerField(source='province.id')
    indicator = CharField(source='indicator.name', read_only=True)
    indicator_id = IntegerField(source='indicator.id')

    class Meta:
        model = IndicatorData
        fields = ('id', 'province', 'province_id', 'indicator', 'indicator_id', 'value', 'unit')


class ProvinceInfoSerializer(serializers.ModelSerializer):
    name = CharField(source='name.name')
    province_id = IntegerField(source='name.id')

    def total_budget(self):
        pass

    class Meta:
        model = ProvinceInfo
        fields = ('id', 'name', 'province_id', 'total_budget', 'active_programmes')


class ProgramDataSerializer(serializers.ModelSerializer):
    program = CharField(source='program.name')
    program_id = IntegerField(source='program.id')

    class Meta:
        model = ProgramData
        fields = ('id', 'program', 'program_id', 'description', 'sectors', 'program_budget')


class CountryDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CountryData
        fields = ('id', 'provinces', 'paalikas', 'municipalities', 'total_population', 'area', 'population_density',
                  'poverty_rate', 'literacy_rate', 'population_under_poverty_line', 'per_capita_income',
                  'human_development_index', 'gdp')


class LayerDataSerializer(serializers.ModelSerializer):

    layer_name = CharField(source='layer_name.name')

    class Meta:
        model = LayerData
        fields = ('id', 'layer_name', 'type', 'file', 'sectors', 'layer_server_url', 'layer_path', 'date', 'source', 'notes')

    def to_representation(self, obj):
        data = super().to_representation(obj)

        if obj.type == 'Raster':
            data.pop('file')

        else:
            data.pop('layer_server_url')
            data.pop('layer_path')

        return data


class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        exclude = ()


class ProgramSpendSerializer(serializers.ModelSerializer):
    program = CharField(source='program.name')
    program_id = IntegerField(source='program.id')
    partners = PartnerSerializer(many=True)

    class Meta:
        model = ProgramData
        fields = ('program', 'program_id', 'program_budget', 'partners', 'total_no_of_partners')


class AreaSerializer(serializers.ModelSerializer):
    programs = ProgramSpendSerializer(many=True)
    total_program_budget = serializers.FloatField(source='total_program_budget.total')

    class Meta:
        model = Area
        fields = ('id', 'hlcit_code', 'type', 'local_name', 'programs', 'total_program_budget', 'total_no_of_programmes')

    def to_representation(self, obj):
        data = super().to_representation(obj)

        if obj.type == 'Not Municipality':
            data.pop('programs')
            data.pop('total_program_budget')
            data.pop('total_no_of_programmes')

        return data


class GlossaryDataSerializer(serializers.ModelSerializer):
    title = CharField(source='title.name')
    source = CharField(source='title.source')
    description = CharField(source='title.glossary')

    class Meta:
        model = GlossaryData
        fields = ('id', 'title', 'source', 'description')


class PdfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pdf
        exclude = ()
