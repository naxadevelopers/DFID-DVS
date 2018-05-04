from django.urls import path, include

from rest_framework import routers

from . import views
from . import viewset


router = routers.DefaultRouter()
router.register(r'users', viewset.UserViewSet)
router.register(r'provinces', viewset.ProvinceViewSet, base_name='provinces-list')
router.register(r'province-data', viewset.ProvinceDataViewSet, base_name='provinces-data')
router.register(r'districts', viewset.DistrictViewSet, base_name='provinces-district-list')
router.register(r'districts-spending', viewset.DistrictSpendingViewSet, base_name='district-spending')
router.register(r'programmes', viewset.ProgramViewSet, base_name='programmes-list')
router.register(r'indicators', viewset.IndicatorViewSet, base_name='indicators-list')
router.register(r'federalism-draft', viewset.FederalismDraftViewSet, base_name='federalism-draft-list')
router.register(r'sectors', viewset.SectorViewSet, base_name='sectors-list')
router.register(r'province-info', viewset.ProvinceInfoViewSet, base_name='province-info-list')
router.register(r'programme-data', viewset.ProgramDataViewSet, base_name='program-data-list')
router.register(r'country-data', viewset.CountryDataViewSet, base_name='country-data-list')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.token),
    path('geojson/country/', views.country_geojson),
    path('geojson/province/<province_id>/', views.province_geojson),

]