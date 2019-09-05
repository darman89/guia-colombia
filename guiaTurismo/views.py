import json
import os
import requests

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
from django_filters import rest_framework as filters

from guiaTurismo.filters import TourFilter
from users.models import User
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
    # for guide in guides_list:
    #   guide.photo = guide.photo.url
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


@api_view(["GET"])
def tours_guide(request, guide_id):
    tours = Tour.objects.filter(guide=guide_id)
    return Response(TourSerializer(tours, many=True).data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def email_view(request):
    jsonEmail = json.loads(request.body)
    tourId = jsonEmail['tourId']
    userId = jsonEmail['userId']
    tour = Tour.objects.get(id=tourId)
    user = User.objects.get(id=userId)
    guide = Guide.objects.get(id=tour.guide.id)

    r = requests.post(
        "https://api.mailgun.net/v3/" + os.environ['MAILGUN_DOMAIN'] + "/messages",
        auth=("api", os.environ['MAILGUN_API_KEY']),
        data={"from": "Guía Colombia <mailgun@" + os.environ['MAILGUN_DOMAIN'] + ">",
              "to": [guide.email],
              "subject": "Hay un Turista interesado en uno de tus Tours",
              "text": "Hola " + guide.name + "! \n" + user.first_name + " " + user.last_name + " está interesado en tu Tour " + tour.name + "\n" +
                      "puedes contactarlo al correo: " + user.email + "\n" + "Saludos, Guias Ágiles Colombia."
              })
    # Return response
    return JsonResponse({"status": r.status_code})


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
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TourFilter
