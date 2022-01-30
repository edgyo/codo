from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def profile(request):
    return HttpResponse("Welcome back to Codo League! You are at home page.")

def register(request):
    return HttpResponse("Welcome back to Codo League! You are at home page.")