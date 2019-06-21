from django.urls import path
from . import views

urlpatterns = [
    # rest-framework
    path(r'group/<int:pk>/', views.GroupDetail.as_view()),
    path(r'group/', views.GroupList.as_view()),
]
