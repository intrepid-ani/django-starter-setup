from django.shortcuts import render
from django.http import HttpResponse # This is just for testing purposes, you can remove this line 

# Create your views here.

def home(request):
    return HttpResponse("Hello, World!") # This is just for testing purposes, you can remove this line