from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout
from company.models import Jobs
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'company/dashboard.html')

def jobs(request):
    user = User.objects.get(username=request.user.username)
    alljobs = Jobs.objects.filter(user=user)
    context = {'alljobs':alljobs}
    #print(alljobs)
    return render(request, 'company/jobs.html', context)


def questions(request):
    return render(request, 'company/questionsbank.html')

def status(request, id):
    job = Jobs.objects.get(id=id)
    job_status = job.job_status
    if job_status:
        job.job_status = False
    else:
        job.job_status = True
    job.save()
    return redirect('/jobs/')

def update(request, id):
    if request.method == "POST":
        # Get the post parameters
        job_title = request.POST['job_title']
        job_discription = request.POST['job_discription']
        
        # Create the job
        ujob = Jobs.objects.get(id=id)
        ujob.job_title = job_title
        ujob.job_discription = job_discription
        ujob.save()
        
        
        messages.success(request, "Your job is updated successfully.")
        return redirect('/jobs/')
        #return render(request, 'company/jobs.html')

    user = User.objects.get(username=request.user.username)
    ujob = Jobs.objects.filter(user=user, id=id)
    print(ujob)
    context = {'ujob':ujob}
    #print(alljobs)
    return render(request, 'company/addjob.html', context)

def delete(request, id):
    job = Jobs.objects.get(id=id)
    job.delete()
    return redirect('/jobs/')

def addquestions(request):
    user = User.objects.get(username=request.user.username)
    alljobs = Jobs.objects.filter(user=user)
    context = {'alljobs':alljobs}
    return render(request, 'company/addquestions.html', context)

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




def addjob(request):
    if request.method == "POST":
        # Get the post parameters
        job_title = request.POST['job_title']
        job_discription = request.POST['job_discription']
        
        # Create the job
        user = User.objects.get(username=request.user.username)
        job = Jobs(user = user, job_title = job_title, job_discription = job_discription)
        job.save()
       
        
        messages.success(request, "Your job is added successfully.")
        return redirect('/jobs/')
        #return render(request, 'company/jobs.html')
    return render(request, 'company/addjob.html')