from django.urls import path
from . import views

urlpatterns = [
    # rest-framework
    path(r'user/<int:pk>/', views.UserDetail.as_view()),
    path(r'user/', views.UserList.as_view()),
    path(r'createUser/', views.CreateUser.as_view()),
    path(r'updateUserPassword/<str:username>/', views.UpdateUserPassword.as_view()),

]
