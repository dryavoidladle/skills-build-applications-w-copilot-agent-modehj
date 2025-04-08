from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Octofit Tracker App!")

def about(request):
    return render(request, 'tracker/about.html')