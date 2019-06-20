from django.contrib.auth.models import (User)
from utils import crud
from .serializers import UserListSerializer
from .serializers import CreateUserSerializer
from .serializers import UpdateUserSerializer


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


class UpdateUser(crud.UpdateMixin):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
