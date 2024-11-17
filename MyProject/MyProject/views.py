from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1> Home Page <h1>")

def welcome(request):
    return render(request, "base.py")