import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Guide


@csrf_exempt
def guides_view(request):
    guides_list = Guide.objects.all()
    cityId = request.GET.get('cityId')
    categoryId = request.GET.get('categoryId')
    if cityId is not None:
        guides_list = guides_list.filter(city__id=cityId)
    if categoryId is not None:
        guides_list = guides_list.filter(category__id=categoryId)
    return HttpResponse(serializers.serialize("json", guides_list))


@csrf_exempt
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


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": 'ok'})


@csrf_exempt
def is_logged_view(request):
    if request.user.is_authenticated:
        message = 'ok'
    else:
        message = 'no'

    return JsonResponse({"message": message})
