from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


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