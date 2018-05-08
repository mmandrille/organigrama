from django.shortcuts import render
from django.http import HttpResponse
#Import Personales

# Create your views here.
def home(request):
    return HttpResponse('Hola mundo')