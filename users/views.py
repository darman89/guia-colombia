from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(GenericViewSet, CreateModelMixin):
    queryset = User.objects.exclude(is_staff=False)
    serializer_class = UserSerializer
