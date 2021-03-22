from django.shortcuts import render, HttpResponse

# Create your views here.
def company(request):
    return HttpResponse('This is company Page')