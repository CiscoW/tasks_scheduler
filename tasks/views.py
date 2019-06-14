from __future__ import absolute_import, unicode_literals
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
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
from utils.crud import CRUD
from utils.crud import CRUDList


# Create your views here.


# Clocked
class ClockedScheduleDetail(CRUD):
    queryset = ClockedSchedule.objects.all()
    serializer_class = ClockedScheduleSerializer


class ClockedScheduleList(CRUDList):
    queryset = ClockedSchedule.objects.all()
    serializer_class = ClockedScheduleSerializer


# Crontab
class CrontabScheduleDetail(CRUD):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer


class CrontabScheduleList(CRUDList):
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer


# Interval
class IntervalScheduleDetail(CRUD):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer


class IntervalScheduleList(CRUDList):
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer


# Solar
class SolarScheduleDetail(CRUD):
    queryset = SolarSchedule.objects.all()
    serializer_class = SolarScheduleSerializer


class SolarScheduleList(CRUDList):
    queryset = SolarSchedule.objects.all()
    serializer_class = SolarScheduleSerializer


# PeriodicTask
class PeriodicTaskDetail(CRUD):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer


class PeriodicTaskList(CRUDList):
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
        resp = {'ok': True, 'detail': r.id}
        return HttpResponse(json.dumps(resp), content_type="application/json")


class Result(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, result_id):
        async_result = AsyncResult(result_id)
        resp = {'ok': True, 'detail': async_result.get()}
        return HttpResponse(json.dumps(resp), content_type="application/json")

# # 非Swagger写法
# def index(request):
#     # print('1 + 1 = ?')
#     r = add.delay(1, 1)
#     # print(type(r))
#     # print('r.get() = %s ' % r.get())
#     resp = {'ok': True, 'detail': r.id}
#     return HttpResponse(json.dumps(resp), content_type="application/json")
#
#
# def get_result(request, result_id):
#     async_result = AsyncResult(result_id)
#     resp = {'ok': True, 'detail': async_result.get()}
#     return HttpResponse(json.dumps(resp), content_type="application/json")
