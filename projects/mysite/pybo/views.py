from django.shortcuts import render
from django.http import HttpResponse

def index(request) : 
    return HttpResponse("pybo입니다.")

# Create your views here.
