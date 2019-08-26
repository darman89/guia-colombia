from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, ObtainAuthToken

router = DefaultRouter()
router.register('user', UserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
]
