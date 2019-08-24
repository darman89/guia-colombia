from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserSerializer


class UserViewSet(GenericViewSet, CreateModelMixin):
    queryset = Costumer.objects.exclude(is_staff=False)
    serializer_class = UserSerializer
