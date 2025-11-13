from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_app2(req):
    return HttpResponse("Learn from app2")