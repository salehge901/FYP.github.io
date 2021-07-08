from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout

from user.camera import VideoCamera

urlpatterns = [

    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam', views.webcam, name="webcam"),


    path('user/home/', views.uhome, name='uhome'),
    path('user/job/', views.ujob, name='ujob'),
    path('user/profile/', views.profile, name='profile'),
    path('user/interview/', views.interview, name='interview'),
    path('user/countdown/<int:id>', views.countdown, name='countdown'),
    path('interview/<int:id>/<int:qid>', views.takeinterview,name='takeinterview'),
    path('user/job/interview-schdule/<int:id>', views.interviewschdule, name='interviewschdule'),
]
