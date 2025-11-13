from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nextTime(request):
    return HttpResponse("I will do it next time fs")