from django.contrib import admin

from core.models import Pdf, Province, District, Sector, Program, ProvinceData, ProgramBudget, DistrictSpending, Indicator, IndicatorData, ProvinceInfo,\
	Partner, CountryData, Layer, LayerData, Area, GlossaryData, Poverty, About

admin.site.site_header = 'DFID'
admin.site.index_title = 'DFID Forms'

admin.site.register(About)
admin.site.register(Pdf)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(Program)
admin.site.register(ProvinceData)
admin.site.register(ProgramBudget)
admin.site.register(DistrictSpending)
admin.site.register(Indicator)
admin.site.register(Partner)
admin.site.register(CountryData)
admin.site.register(Layer)
admin.site.register(LayerData)
admin.site.register(Area)
admin.site.register(GlossaryData)
admin.site.register(IndicatorData)
admin.site.register(ProvinceInfo)
admin.site.register(Poverty)




