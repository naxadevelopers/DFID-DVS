from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from .models import ProvinceData


class ProvinceDataSerializer(ModelSerializer):

    class Meta:
        model = ProvinceData
        fields = '__all__'