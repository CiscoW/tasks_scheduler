from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClockedScheduleDetail
from .views import index
from .views import get_result

urlpatterns = [
    # rest-framework
    path(r'clocked/<int:pk>/', ClockedScheduleDetail.as_view()),
    path(r'clocked/', ClockedScheduleDetail.as_view()),

    # celery 使用样例接口
    url(r'index', index),
    path(r'get_result/<str:result_id>', get_result),

]

urlpatterns = format_suffix_patterns(urlpatterns)
