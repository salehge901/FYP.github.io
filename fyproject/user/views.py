from django.shortcuts import render, HttpResponse

# Create your views here.
def user(request):
    return HttpResponse('This is user Page')