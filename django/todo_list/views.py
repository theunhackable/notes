from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

def index(requests):
    return HttpResponse("<h1> Hello world</h1>")