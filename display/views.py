from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the home page!")

def staff(request):
    return HttpResponse("Welcome to the staff page")