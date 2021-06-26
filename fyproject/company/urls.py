from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout

urlpatterns = [
    path('company/dashboard/', views.dashboard, name='dashboard'),
    path('company/jobs/', views.jobs, name='jobs'),
    path('company/profile/', views.profile, name='profile'),
    path('company/jobs/add-job/', views.addjob, name='addjob'),
    path('company/questions/', views.questions, name='questions'),
    path('company/questions/<int:id>', views.jquestions, name='jquestions'),
    path('company/questions/add-new-questions/', views.addquestions, name='addquestions'),
    path('company/candidate/', views.candidate, name='candidate'),
    path('company/interview/', views.interview, name='interview'),
    path('logout', views.ulogout, name='ulogout'),
    path('jobs/<int:id>', views.status,name='status'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('company/job/update/<int:id>', views.update,name='update'),
    path('qstatus/<int:id>', views.qstatus,name='qstatus'),
    path('qdelete/<int:id>', views.qdelete,name='qdelete'),
    path('company/question/qupdate/<int:id>', views.qupdate,name='qupdate'),


]
