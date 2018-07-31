from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import Pdf, Province, District, Sector, Program, ProvinceData, ProgramBudget, DistrictSpending, Indicator, IndicatorData, ProvinceInfo, ProgramData,\
	Partner, CountryData, SectorData, Layer, LayerData, Area, GlossaryData, Poverty

admin.site.site_header = 'DFID'
admin.site.index_title = 'DFID Forms'

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
admin.site.register(SectorData)
admin.site.register(Layer)
admin.site.register(LayerData)
admin.site.register(Area)
admin.site.register(GlossaryData)
admin.site.register(IndicatorData)
admin.site.register(ProvinceInfo)
admin.site.register(ProgramData)
admin.site.register(Poverty)




