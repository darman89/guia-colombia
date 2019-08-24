from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
