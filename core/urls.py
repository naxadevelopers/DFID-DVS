from django.urls import path, include

from rest_framework import routers, serializers, viewsets

from . import views
from . import viewset


router = routers.DefaultRouter()
router.register(r'users', viewset.UserViewSet)
router.register(r'provinces', viewset.ProvinceViewSet, base_name='provinces-list')
router.register(r'provinces-edit', viewset.ProvinceUpdateViewSet, base_name='provinces-edit')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.token),
    path('province-data-create/', views.province_data_create)


]