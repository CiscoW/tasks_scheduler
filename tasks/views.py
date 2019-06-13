from __future__ import absolute_import, unicode_literals
import json
from django.http import HttpResponse
from celery.result import AsyncResult
from django_celery_beat.models import ClockedSchedule
from .serializers import ClockedScheduleSerializer
from .tasks import add
from utils.crud import CRUD


# Create your views here.


# CRUD
class ClockedScheduleDetail(CRUD):
    queryset = ClockedSchedule.objects.all()
    serializer_class = ClockedScheduleSerializer


# 异步任务测试样例
def index(request):
    # print('1 + 1 = ?')
    r = add.delay(1, 1)
    # print(type(r))
    # print('r.get() = %s ' % r.get())
    resp = {'ok': True, 'detail': r.id}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_result(request, result_id):
    async_result = AsyncResult(result_id)
    resp = {'ok': True, 'detail': async_result.get()}
    return HttpResponse(json.dumps(resp), content_type="application/json")