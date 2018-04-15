from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
)
from rest_framework.filters import SearchFilter

from .models import ProvinceData
from .serializers import ProvinceDataSerializer


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets for listing the Province data.
class ProvinceViewSet(
                        CreateModelMixin,
                        ListModelMixin,
                        GenericViewSet):

    serializer_class = ProvinceDataSerializer
    filter_backends = [SearchFilter]
    search_fields = ['province__name', 'total_population', 'area', 'population_desnity', 'poverty_rate',
                     'population_under_poverty_line', 'per_capita_income', 'hh_by_lowest_wealth_quantiles',
                     'human_development_index', 'minute_access_to', 'vulnerability_index', 'gdp']

    queryset = ProvinceData.objects.select_related()

    def get_queryset(self):
        province_query = self.request.GET.get('province')

        if province_query:
            queryset = self.queryset.filter(province=province_query)

            return queryset
        else:
            queryset = self.queryset
            return queryset


# ViewSets for updating the particular Province.
class ProvinceUpdateViewSet(
                                UpdateModelMixin,
                                RetrieveModelMixin,
                                GenericViewSet
                            ):
    serializer_class = ProvinceDataSerializer
    queryset = ProvinceData.objects.all()