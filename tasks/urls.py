from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # rest-framework
    path(r'clocked/<int:pk>/', views.ClockedScheduleDetail.as_view()),
    path(r'clocked/', views.ClockedScheduleDetail.as_view()),

    # celery 使用样例接口
    url(r'index', views.Add.as_view()),
    path(r'get_result/<str:result_id>', views.Result.as_view()),

]
