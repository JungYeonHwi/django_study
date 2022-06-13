from django.shortcuts import render
from django.http import HttpResponse

def index(request) : 
    return HttpResponse("안녕하세요 pybo 입니다.")

# Create your views here.
