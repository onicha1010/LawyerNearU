from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Home</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def form(request):
    return HttpResponse("<h1>Form</h1>")