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


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.token),
    path('geojson/country/', views.country_geojson),
    path('geojson/province/<province_id>/', views.province_geojson),

]