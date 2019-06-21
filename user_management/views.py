from django.contrib.auth.models import (User)
from rest_framework.permissions import IsAuthenticated

from utils import crud
from utils.permissions import IsOneSelf
from .serializers import UserListSerializer
from .serializers import CreateUserSerializer
from .serializers import UpdateUserPasswordSerializer


# Create your views here.

# users
class UserDetail(crud.RetrieveMixin,
                 crud.UpdateMixin,
                 crud.DeleteMixin):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserList(crud.RetrieveListMixin):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class CreateUser(crud.CreateMixin):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserPassword(crud.UpdateMixin):
    lookup_field = 'username'
    permission_classes = (IsAuthenticated, IsOneSelf)
    queryset = User.objects.all()
    serializer_class = UpdateUserPasswordSerializer
