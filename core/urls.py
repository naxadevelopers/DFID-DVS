from django.urls import path, include

from rest_framework import routers, serializers, viewsets

from . import views
from . import viewset


router = routers.DefaultRouter()
router.register(r'users', viewset.UserViewSet)
router.register(r'provinces', viewset.ProvinceViewset, base_name='provinces-list')
router.register(r'province-data', viewset.ProvinceDataViewSet, base_name='provinces-data')
router.register(r'districts', viewset.DistrictViewset, base_name='provinces-district-list')
router.register(r'districts-spending', viewset.DistrictSpendingViewset, base_name='district-spending')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.token),
    path('geojson/country/', views.country_geojson),

]