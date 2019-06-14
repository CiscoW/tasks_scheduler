from django.urls import path
from . import views

urlpatterns = [
    # rest-framework
    path(r'clocked/<int:pk>/', views.ClockedScheduleDetail.as_view()),
    path(r'clocked/', views.ClockedScheduleList.as_view()),

    path(r'crontab/<int:pk>/', views.CrontabScheduleDetail.as_view()),
    path(r'crontab/', views.CrontabScheduleList.as_view()),

    path(r'interval/<int:pk>/', views.IntervalScheduleDetail.as_view()),
    path(r'interval/', views.IntervalScheduleList.as_view()),

    path(r'solar/<int:pk>/', views.SolarScheduleDetail.as_view()),
    path(r'solar/', views.SolarScheduleList.as_view()),

    path(r'periodicTask/<int:pk>/', views.PeriodicTaskDetail.as_view()),
    path(r'periodicTask/', views.PeriodicTaskList.as_view()),

    # celery 使用样例接口
    path(r'index', views.Add.as_view()),
    path(r'get_result/<str:result_id>', views.Result.as_view()),

]
