from django.shortcuts import render, HttpResponse ,redirect
from vib.models import Contact, extenduser
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django  import  forms
from vib.models import  Count , Extend
from django.views.generic import  DetailView
import  sqlite3

# Create your views here.


def home(request):
    return render(request, 'vib/home.html')

def features(request):
    return render(request, 'vib/features.html')

def about(request):
    return render(request, 'vib/about.html')

def contact(request):
    if request.method == "POST":
        # Get the post parameters
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name= name , email = email , subject = subject , message = message)
        contact.save()
        return redirect("/contact")
    return render(request, 'vib/contact.html')

def handlelogin(request):
    if request.method == "POST":
        # Get the post parameters

        lusername = request.POST['lusername']
        lpassword = request.POST['lpassword']

        user = authenticate(username=lusername, password=lpassword)
        extendobject = Extend.objects.all()
        type = ''
        for itme in extendobject:
            if(itme.user==user):
                type = itme.source_name
                break
        print(type)
        if user is not None:
            login(request  , user)
            if(type=="Candidate"):
                return render(request, 'vib/home.html')
            if(type=="Company"):
                return render(request, 'vib/features.html')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")
    return render(request, 'vib/login.html')

def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        setpassword = request.POST['setpassword']
        cpassword = request.POST['cpassword']
        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')
        if setpassword != cpassword:
            messages.error(request, " Passwords do not match")
            return redirect('signup')

        # Create the user
        myuser = User.objects.create_user(username, email, setpassword)
        source_name = request.POST['source_name']
        newextenduser = Extend(source_name = source_name , user=myuser)
        newextenduser.save()
        myuser.save()
        return render(request, 'vib/home.html')
    else:
          return render(request, 'vib/signup.html')

def countdown(request):

 return render(request, 'vib/countdown.html')
def handelLogout(request):
    logout(request)
    return render(request, 'vib/home.html')
def Schedule(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        date = request.POST['date']
        time = request.POST['time']
        Schdule = Count(date=date, time=time, user=user)
        Schdule.save()
        return render(request, 'vib/home.html')
    return render(request, 'vib/Schedule.html')