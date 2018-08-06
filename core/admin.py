from django.contrib import admin
from import_export.widgets import ForeignKeyWidget

from core.models import Pdf, Province, District, Sector, Program, ProvinceData, ProgramBudget, DistrictSpending, Indicator, IndicatorData, ProvinceInfo,\
	Partner, CountryData, Layer, LayerData, Area, GlossaryData, Poverty, About, ProgramData
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

admin.site.site_header = 'DFID'
admin.site.index_title = 'DFID Forms'


class IndicatorResource(resources.ModelResource):

	class Meta:
		model = Indicator
		import_id_fields = ('name',)
		exclude = ('id',)


class IndicatorDataResource(resources.ModelResource):
	province = Field(
		column_name='province',
		attribute='province',
		widget=ForeignKeyWidget(Province, 'name'))

	indicator = Field(
		column_name='indicator',
		attribute='indicator',
		widget=ForeignKeyWidget(Indicator, 'name'))

	class Meta:
		model = IndicatorData
		fields = ('id', 'province', 'indicator', 'value', 'unit', 'years', 'source')


class LayerDataResource(resources.ModelResource):

	layer_name = Field(
		column_name='layer_name',
		attribute='layer_name',
		widget=ForeignKeyWidget(Layer, 'name'))

	class Meta:
		model = LayerData
		import_id_fields = ('layer_name',)
		fields = ('layer_name', 'source', 'date', 'type', 'notes')


class ProvinceDataResource(resources.ModelResource):
	province = Field(
		column_name='province',
		attribute='province',
		widget=ForeignKeyWidget(Province, 'name'))

	class Meta:
		model = ProvinceData
		import_id_fields = ('province',)
		fields = ('province', 'total_population', 'area', 'population_density', 'poverty_rate', 'population_under_poverty_line',
				  'per_capita_income', 'hh_by_lowest_wealth_quantiles', 'human_development_index', 'minute_access_to', 'vulnerability_index',
				  'gdp')


class PovertyResource(resources.ModelResource):
	hlcit_code = Field(
		column_name='hlcit_code',
		attribute='hlcit_code',
		widget=ForeignKeyWidget(Area, 'hlcit_code'))

	class Meta:
		model = Poverty
		import_id_fields = ('hlcit_code',)
		fields = ('lgu', 'hlcit_code', 'lu_type', 'lgu_FGT_0', 'lgu_FGT_1', 'lgu_FGT_2', 'female_lit_rate', 'male_lit_rate', 'total_lit_rate')


class DistrictSpendingResource(resources.ModelResource):
	program = Field(
		column_name='program',
		attribute='program',
		widget=ForeignKeyWidget(Program, 'name'))

	district = Field(
		column_name='district',
		attribute='district',
		widget=ForeignKeyWidget(District, 'name'))

	class Meta:
		model = DistrictSpending
		import_id_fields = ('id',)
		fields = ('id', 'district', 'program', 'annual_spend')


class AreaResource(resources.ModelResource):
	# programs = Field(
	# 	column_name='programs',
	# 	attribute='programs',
	# 	widget=ManyToManyWidget(ProgramData, 'program.name'))

	province = Field(
		column_name='province',
		attribute='province',
		widget=ForeignKeyWidget(Province, 'name'))

	class Meta:
		model = Area
		import_id_fields = ('hlcit_code',)
		fields = ('hlcit_code', 'province', 'type', 'local_name', 'programs')

	def dehydrate_programs(self, accession):
		programs = [pro.program.name for pro in accession.programs.all()]
		programs = ','.join(programs)

		return '%s' % programs


class LayerDataAdmin(ImportExportModelAdmin):

	search_fields = ('layer_name__name',)
	list_display = ['layer_name', 'source', 'date', 'type', 'notes', 'file', 'layer_server_url', 'layer_path']
	resource_class = LayerDataResource


class ProvinceDataAdmin(ImportExportModelAdmin):
	resource_class = ProvinceDataResource
	list_display = ['province', 'total_population', 'area', 'population_density', 'poverty_rate', 'population_under_poverty_line',
					'per_capita_income', 'hh_by_lowest_wealth_quantiles', 'human_development_index', 'minute_access_to', 'vulnerability_index', 'gdp']


class DistrictSpendingAdmin(ImportExportModelAdmin):
	resource_class = DistrictSpendingResource
	list_display = ['district', 'program', 'annual_spend']
	search_fields = ('district__name', 'program__name')


class PovertyAdmin(ImportExportModelAdmin):
	list_display = ['lgu', 'lu_type', 'lgu_FGT_0', 'lgu_FGT_1', 'lgu_FGT_2', 'female_lit_rate', 'male_lit_rate', 'total_lit_rate']
	search_fields = ('lgu', 'lu_type')
	resource_class = PovertyResource


class AreaAdmin(ImportExportModelAdmin):
	search_fields = ('hlcit_code', 'local_name', 'province__name', 'type')
	list_display = ['hlcit_code', 'local_name', 'province', 'type']
	resource_class = AreaResource
	#
	# def programs(self, obj):
	# 	return ", ".join([pr.program.name for pr in obj.programs.all()])


class IndicatorAdmin(ImportExportModelAdmin):
	resource_class = IndicatorResource
	search_fields = ('name',)
	list_display = ['name', 'source', 'glossary']


class IndicatorDataAdmin(ImportExportModelAdmin):
	search_fields = ('indicator__name',)
	list_display = ['province', 'indicator', 'value', 'unit', 'years', 'source']
	resource_class = IndicatorDataResource


class ProvinceInfoAdmin(admin.ModelAdmin):
	list_display = ['name', 'total_budget']
	search_fields = ('name__name',)


class SectorAdmin(admin.ModelAdmin):
	list_display = ['name', 'code']
	search_fields = ('name', 'code')


class ProgramBudgetAdmin(admin.ModelAdmin):
	list_display = ['program', 'budget']


class DistrictAdmin(admin.ModelAdmin):
	search_fields = ('name', 'province__name')
	list_display = ['name', 'province']


class LayerAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	list_display = ['name', 'sectors']

	def sectors(self, obj):
		return ", ".join([sector.name for sector in obj.sector.all()])


class CountryDataAdmin(admin.ModelAdmin):
	list_display = ['provinces', 'paalikas', 'municipalities', 'total_population', 'area', 'population_density', 'poverty_rate',
					'literacy_rate', 'population_under_poverty_line', 'per_capita_income', 'human_development_index', 'gdp']


admin.site.register(About)
admin.site.register(Pdf)
admin.site.register(Province)
admin.site.register(District, DistrictAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Program)
admin.site.register(ProvinceData, ProvinceDataAdmin)
admin.site.register(ProgramBudget, ProgramBudgetAdmin)
admin.site.register(DistrictSpending, DistrictSpendingAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Partner)
admin.site.register(CountryData, CountryDataAdmin)
admin.site.register(Layer, LayerAdmin)
admin.site.register(LayerData, LayerDataAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(GlossaryData)
admin.site.register(IndicatorData, IndicatorDataAdmin)
admin.site.register(ProvinceInfo, ProvinceInfoAdmin)
admin.site.register(Poverty, PovertyAdmin)







