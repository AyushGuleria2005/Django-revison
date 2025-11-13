from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_app1(req,**kwargs):
    key = kwargs.get("key")
    return HttpResponse(f"Learn from app1 - {key}")