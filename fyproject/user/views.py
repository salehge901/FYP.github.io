
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout
from company.models import Jobs, QuestionBank
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request, 'user/dashboard.html')