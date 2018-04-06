from django.urls import path, include

from rest_framework import routers, serializers, viewsets

from . import views
from . import viewset


router = routers.DefaultRouter()
router.register(r'users', viewset.UserViewSet)

urlpatterns = [
    path('home', views.index, name='index'),
    path('', include(router.urls)),
    path('api-token-auth/', views.token)

]