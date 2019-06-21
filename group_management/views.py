from django.contrib.auth.models import Group
from .serializers import GroupSerializer
from utils import crud


# Create your views here.
class GroupDetail(crud.RetrieveMixin,
                  crud.UpdateMixin,
                  crud.DeleteMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupList(crud.RetrieveListMixin,
                crud.CreateMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
