from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout


# Create your views here.
def dashboard(request):
    return render(request, 'company/dashboard.html')

def jobs(request):
    return render(request, 'company/jobs.html')

def addjob(request):
    return render(request, 'company/addjob.html')

def questions(request):
    return render(request, 'company/questionsbank.html')

def addquestions(request):
    return render(request, 'company/addquestions.html')

def candidate(request):
    return render(request, 'company/candidate.html')

def interview(request):
    return render(request, 'company/interview.html')


def ulogout(request):
    logout(request)
    try:
        del request.session['Utype']
    except KeyError:
        pass
    return render(request, 'vib/home.html')

