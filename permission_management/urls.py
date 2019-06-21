from django.urls import path
from . import views

urlpatterns = [
    # rest-framework
    path(r'permission/<int:pk>/', views.PermissionDetail.as_view()),
    path(r'permission/', views.PermissionList.as_view()),
]
