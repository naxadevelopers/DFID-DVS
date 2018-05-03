from django.contrib.auth.models import User

from rest_framework import serializers, viewsets
from rest_framework.filters import SearchFilter

from .models import ProvinceData, Province, District, Program, Partner, DistrictSpending
from .serializers import ProvinceDataSerializer, ProvinceSerializer, DistrictSerializer, ProgramSerializer, \
    PartnerSerializer, DistrictSpendingSerializer


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
class ProvinceDataViewSet(viewsets.ReadOnlyModelViewSet):
    """

    list: list of province data.
    detail: To find detail of one province, append /province_id/

    """
    serializer_class = ProvinceDataSerializer
    filter_backends = [SearchFilter]
    search_fields = ['province__name', 'total_population', 'area', 'population_density', 'poverty_rate',
                     'population_under_poverty_line', 'per_capita_income', 'hh_by_lowest_wealth_quantiles',
                     'human_development_index', 'minute_access_to', 'vulnerability_index', 'gdp']

    queryset = ProvinceData.objects.select_related()

    def get_queryset(self):
        province_query = self.request.query_params.get('province')

        if province_query:
            queryset = self.queryset.filter(province__name='Province '+str(province_query))

            return queryset
        else:
            queryset = self.queryset
            return queryset


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    """

    list:Return the list of all provinces.

    """
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """

    list:Return the list of all districts.

    """
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class DistrictSpendingViewSet(viewsets.ReadOnlyModelViewSet):
    """

    list: list of district spending data.

    """

    serializer_class = DistrictSpendingSerializer
    queryset = DistrictSpending.objects.all()

    def get_queryset(self):
        province_query = self.request.query_params.get('province')

        if province_query:
            queryset = self.queryset.filter(district__province__name='Province '+str(province_query))

            return queryset
        else:
            queryset = self.queryset
            return queryset


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """

    list: list of programmes.

    """

    serializer_class = ProgramSerializer
    queryset = Program.objects.all()