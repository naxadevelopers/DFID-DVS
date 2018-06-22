import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import UpdateView, ListView, CreateView
from django.shortcuts import redirect, get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import reverse

from .models import LayerData, Area, Pdf, Province, Partner
from .forms import LayerDataform


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


# @api_view(['GET'])
# def province_geojson(request, province_id):
#     """
#     detail of particular province geojson
#     """
#     data = {}
#     try:
#         with open('jsons/{}.json'.format(province_id)) as f:
#             data = json.load(f)
#     except:
#         return Response(data, status=status.HTTP_404_NOT_FOUND)
#     return Response(data)
#
#
# @api_view(['GET'])
# def country_geojson(request):
#     """
#     list of country geojson
#     """
#     data = {}
#     try:
#         with open('jsons/province.json') as f:
#             data = json.load(f)
#     except:
#         pass
#
#     return Response(data)
#
#
# @api_view(['GET'])
# def municipalities_geojson(request):
#     """
#     municipalities geojson
#     """
#     data = {}
#     try:
#         with open('jsons/munis.json') as f:
#             data = json.load(f)
#     except:
#         pass
#
#     return Response(data)
#
#
# @api_view(['GET'])
# def ipssj_geojson(request):
#     """
#     ipssj program geojson
#     """
#     data = {}
#     try:
#         with open('jsons/ipssj_jan18_small.json') as f:
#             data = json.load(f)
#     except:
#         pass
#
#     return Response(data)


class LayerDatafileView(UpdateView):
    model = LayerData
    form_class = LayerDataform


class AreaUpdateView(UpdateView):
    model = Area
    fields = '__all__'

    def get_success_url(self):
        return reverse("core:area_list")


class AreaListView(ListView):
    model = Area
    fields = '__all__'


class PdfFormView(CreateView):
    model = Pdf
    fields = ('pdf',)

    def get_success_url(self):
        return reverse("core:pdf_list")


class PdfListView(ListView):
    model = Pdf


class PartnerUpdateView(UpdateView):
    model = Partner
    fields = '__all__'

    def get_success_url(self):
        return reverse("core:partner_list")


class PartnerListView(ListView):
    model = Partner
