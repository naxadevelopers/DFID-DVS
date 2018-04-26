from django.urls import path, include

from rest_framework import routers

from . import views
from . import viewset


router = routers.DefaultRouter()
router.register(r'users', viewset.UserViewSet)
router.register(r'provinces', viewset.ProvinceViewset, base_name='provinces-list')
router.register(r'province-data', viewset.ProvinceDataViewSet, base_name='provinces-data')
router.register(r'districts', viewset.DistrictViewset, base_name='provinces-district-list')
router.register(r'districts-spending', viewset.DistrictSpendingViewset, base_name='district-spending')
router.register(r'geojson/country', viewset.CountryGeojsonViewSet, base_name='country-geojson')
router.register(r'geojson/province/<province_id>/', viewset.ProvinceGeojsonViewSet, base_name='province-geojson')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.token),

]