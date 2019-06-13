from __future__ import absolute_import, unicode_literals
import time
import requests
from celery import shared_task


@shared_task
def add(x, y):
    time.sleep(5)
    print("异步测试样例")
    return x + y


@shared_task(ignore_result=True)  # 关闭任务执行结果
def req_task(*args, **kwargs):
    requests.request(*args, **kwargs)
