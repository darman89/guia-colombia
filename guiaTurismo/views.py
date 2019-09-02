import json
from tokenize import Token

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from guiaTurismo.filters import TourFilter
from .models import Guide, City, Category, Tour
from .serializers import GuideSerializer, TourSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def guides_view(request):
    guides_list = Guide.objects.all().prefetch_related('city').prefetch_related('category')
    cityId = request.GET.get('cityId')
    categoryId = request.GET.get('categoryId')
    if cityId is not None:
        guides_list = guides_list.filter(city__id=cityId)
    if categoryId is not None:
        guides_list = guides_list.filter(category__id=categoryId)
    for guide in guides_list:
        guide.photo = guide.photo.url
    serializer_class = GuideSerializer(guides_list, many=True)
    response = Response(serializer_class.data, status=status.HTTP_200_OK, )
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cities_view(request, city_id=None):
    cities_list = City.objects.all()
    if city_id is not None:
        cities_list = cities_list.filter(id=city_id)
    return HttpResponse(serializers.serialize("json", cities_list), content_type="application/json")


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def categories_view(request, category_id=None):
    categories_list = Category.objects.all()
    if category_id is not None:
        categories_list = categories_list.filter(id=category_id)
    return HttpResponse(serializers.serialize("json", categories_list), content_type="application/json")


def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Nombre de usuario o contraseña incorrectos'
    return JsonResponse({"message": message})


def logout_view(request):
    logout(request)
    return JsonResponse({"message": 'ok'})


def is_logged_view(request):
    if request.user.is_authenticated:
        message = 'ok'
    else:
        message = 'no'
    return JsonResponse({"message": message})


class ToursList(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filter_class = TourFilter
    permission_classes = (IsAuthenticated,)
