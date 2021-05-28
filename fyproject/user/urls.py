from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout

urlpatterns = [
    path('user/home/', views.uhome, name='uhome'),
    path('user/job/', views.ujob, name='ujob'),
    path('user/job/interview-schdule/<int:id>', views.interviewschdule, name='interviewschdule'),
]
