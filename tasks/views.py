from __future__ import absolute_import, unicode_literals

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult
from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import SolarSchedule
from django_celery_beat.models import PeriodicTask
from .serializers import ClockedScheduleSerializer
from .serializers import CrontabScheduleSerializer
from .serializers import IntervalScheduleSerializer
from .serializers import SolarScheduleSerializer
from .serializers import PeriodicTaskSerializer
from .tasks import add
from utils import crud


# Create your views here.


# Clocked
class ClockedScheduleDetail(crud.RetrieveMixin,
                            crud.UpdateMixin,
                            crud.DeleteMixin):
    queryset = ClockedSchedule.objects.all()
    serializer_class = ClockedScheduleSerializer


class ClockedScheduleList(crud.CreateMixin,
                          crud.RetrieveListMixin):
    queryset = ClockedSchedule.objects.all()
    serializer_class = ClockedScheduleSerializer


# Crontab
class CrontabScheduleDetail(crud.RetrieveMixin,
                            crud.UpdateMixin,
                            crud.DeleteMixin):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer


class CrontabScheduleList(crud.CreateMixin,
                          crud.RetrieveListMixin):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer


# Interval
class IntervalScheduleDetail(crud.RetrieveMixin,
                             crud.UpdateMixin,
                             crud.DeleteMixin):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer


class IntervalScheduleList(crud.CreateMixin,
                           crud.RetrieveListMixin):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer


# Solar
class SolarScheduleDetail(crud.RetrieveMixin,
                          crud.UpdateMixin,
                          crud.DeleteMixin):
    queryset = SolarSchedule.objects.all()
    serializer_class = SolarScheduleSerializer


class SolarScheduleList(crud.CreateMixin,
                        crud.RetrieveListMixin):
    queryset = SolarSchedule.objects.all()
    serializer_class = SolarScheduleSerializer


# PeriodicTask
class PeriodicTaskDetail(crud.RetrieveMixin,
                         crud.UpdateMixin,
                         crud.DeleteMixin):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer


class PeriodicTaskList(crud.CreateMixin,
                       crud.RetrieveListMixin):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer


# 异步任务测试样例 Swagger写法
class Add(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        print('1 + 1 = ?')
        r = add.delay(1, 1)
        # print(type(r))
        # print('r.get() = %s ' % r.get())
        resp = {'id': r.id}
        return Response(resp, content_type="application/json")


class Result(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, result_id):
        async_result = AsyncResult(result_id)
        resp = {'result': async_result.get()}
        return Response(resp, content_type="application/json")
