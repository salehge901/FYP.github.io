from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.ulogin, name='ulogin'),
    path('logout/', views.ulogout, name='ulogout'),
    path('signup/', views.signup, name='signup'),
    path('schedule/', views.schedule, name='schedule'),
    path('company/dashboard/', views.cdasboard, name='cdashboard'),
    path('user/home/', views.uhome, name='uhome'),
]
