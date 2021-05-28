
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout
from company.models import Jobs, QuestionBank, Interview
from django.contrib import messages


# Create your views here.
def uhome(request):
    return render(request, 'user/home.html')

def ujob(request):
    user = User.objects.get(username=request.user.username)
    alljobs = Jobs.objects.all()
    context = {'alljobs':alljobs}
    return render(request, 'user/job.html',context)

def interviewschdule(request, id):
    alljobs = Jobs.objects.all()
    context = {'alljobs':alljobs}
    return render(request, 'user/job.html',context)