from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import ProvinceData, Province


def index(request):
    return HttpResponse("Hello, world. You're at the dfid index.")


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def token(request):
    user = User.objects.first()
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user_id': user.pk,
        'email': user.email
    })


def province_data_create(request):
    df = pd.read_excel('core/province.xlsx')
    try:
        provinces = [
            ProvinceData(
                    province=Province.objects.get(name=row),
                    total_population=df.ix[row]['Indicator 1'],
                    area=float(df.ix[row]['Unnamed: 1']),
                    population_desnity=int(df.ix[row]['Indicator 2']),
                    poverty_rate=df.ix[row]['Indicator 3'],
                    population_under_poverty_line=int(df.ix[row]['Indicator 4']),
                    per_capita_income=df.ix[row]['Indicator 5'],
                    hh_by_lowest_wealth_quantiles=df.ix[row]['Indicator 6'],
                    gdp=int(df.ix[row]['Indicator 10']),
                    human_development_index=df.ix[row]['Indicator 7'],
                    minute_access_to=df.ix[row]['Indicator 8'],
                    vulnerability_index=df.ix[row]['Indicator 9'],

            )for row in range(1, 8)
        ]
        ProvinceData.objects.bulk_create(provinces)
    except Province.DoesNotExist:
        pass
    return HttpResponse('successfully loaded provinces data')
