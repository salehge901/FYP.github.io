from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.CharField(max_length=122)
class extenduser(models.Model):
    source_name = models.CharField(max_length= 15)
    user = models.OneToOneField(User , on_delete=models.CASCADE)

class Count(models.Model):

    date = models.DateField()
    time = models.TimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Extend(models.Model):
    source_name = models.CharField(max_length= 15)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
