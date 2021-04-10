from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'vib'

urlpatterns = [
    path('', views.home, name='home'),
    path('features', views.features, name='features'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.handlelogin, name='handlelogin'),
    path('signup', views.signup, name='signup'),
    path('countdown', views.countdown, name='countdown'),
    path('logout', views.handelLogout, name="handleLogout"),
    path('Schedule', views.Schedule, name="handleLogout")

]
