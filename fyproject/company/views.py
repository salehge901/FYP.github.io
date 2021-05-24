from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate,  login, logout
from company.models import Jobs, QuestionBank
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
    user = User.objects.get(username=request.user.username)
    allquestions = QuestionBank.objects.filter(user=user)
    alljobs = Jobs.objects.filter(user=user) 
    context = {'allquestions':allquestions,'alljobs':alljobs}
    #print(alljobs)
    return render(request, 'company/questionsbank.html', context)

def jquestions(request, id):
    user = User.objects.get(username=request.user.username)
    ujob = Jobs.objects.get(id=id)
    # print(ujob.job_title)
    allquestions = QuestionBank.objects.filter(user=user, job=ujob)
    alljobs = Jobs.objects.filter(user=user)
    #print(allquestions)
    context = {'allquestions':allquestions,'alljobs':alljobs,'id':id}
    #print(alljobs)
    #return redirect('/questions/')
    return render(request, 'company/questionsbank.html', context)

def status(request, id):
    job = Jobs.objects.get(id=id)
    job_status = job.job_status
    if job_status:
        job.job_status = False
    else:
        job.job_status = True
    job.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    #return redirect('/jobs/')

def qstatus(request, id):
    question = QuestionBank.objects.get(id=id)
    question_status = question.question_status
    if question_status:
        question.question_status = False
    else:
        question.question_status = True
    question.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # return redirect('/questions/')

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
    #print(ujob)
    context = {'ujob':ujob}
    #print(alljobs)
    return render(request, 'company/addjob.html', context)

def qupdate(request, id):
    if request.method == "POST":
        # Get the post parameters
        job_title = request.POST['jobddl']
        question = request.POST['question']
        answer = request.POST['answer']
        timeddl = request.POST['timeddl']
       
        job = Jobs.objects.get(job_title=job_title)
        uquestion = QuestionBank.objects.get(id=id)
        uquestion.job = job
        uquestion.question = question
        uquestion.answer = answer
        uquestion.time = timeddl
        
        uquestion.save()
       
        
        messages.success(request, "Your Question is updated successfully.")
        return redirect('/questions/')
        #return render(request, 'company/jobs.html')

    user = User.objects.get(username=request.user.username)
    uquestion = QuestionBank.objects.filter(user=user, id=id)
    alljobs = Jobs.objects.filter(user=user)
    #print(uquestion[0].job.job_title)
    #print(alljobs[0].job_title)
    #print(alljobs[0].user)

    context = {'uquestion':uquestion,'alljobs':alljobs}
    #print(alljobs)
    return render(request, 'company/addquestions.html', context)

def delete(request, id):
    job = Jobs.objects.get(id=id)
    job.delete()
    messages.success(request, "Your job is deleted successfully.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    #return redirect('/jobs/')

def qdelete(request, id):
    questtion = QuestionBank.objects.get(id=id)
    questtion.delete()
    messages.success(request, "Your Question is deleted successfully.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    #return redirect('/questions/')

def addquestions(request):
    if request.method == "POST":
        # Get the post parameters
        job_title = request.POST['jobddl']
        question = request.POST['question']
        answer = request.POST['answer']
        timeddl = request.POST['timeddl']
        # Create the job
        user = User.objects.get(username=request.user.username)
        job = Jobs.objects.get(job_title=job_title)
       
        questionBank = QuestionBank(user = user, job = job, question = question, answer = answer, time = timeddl)
        questionBank.save()
       
        
        messages.success(request, "Your Question is added successfully.")
        return redirect('/questions/')
        #return render(request, 'company/jobs.html')
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
    return redirect('/')
    #return render(request, 'vib/home.html')




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