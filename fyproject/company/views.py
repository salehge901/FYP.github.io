from django.shortcuts import render, HttpResponse

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