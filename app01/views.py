from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def home1(request):
    return HttpResponseRedirect("/static/index.html")