from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def learn_python(request):
    return HttpResponse("Hello world from view")

def about(request):
    return HttpResponse('<h1>This is my about<h1/>')