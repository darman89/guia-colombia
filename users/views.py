from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserSerializer
from .models import User


class UserViewSet(GenericViewSet, CreateModelMixin):
    queryset = User.objects.exclude(is_staff=False)
    serializer_class = UserSerializer

