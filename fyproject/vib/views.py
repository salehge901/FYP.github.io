from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'vib/home.html')

def features(request):
    return render(request, 'vib/features.html')

def about(request):
    return render(request, 'vib/about.html')

def contact(request):
    return render(request, 'vib/contact.html')

def login(request):
    return render(request, 'vib/login.html')

def signup(request):
    return render(request, 'vib/signup.html')

def schedule(request):
    return render(request, 'vib/schedule.html')


