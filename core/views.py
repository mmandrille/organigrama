from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, timedelta
#Import Personales
from .models import Organismo, Funcionario

# Create your views here.
def home(request):
    #Obtenemos todos los organismos
    origen = Organismo.objects.get(padre=None, activo=True)
    return render(request, 'home.html', {'origen': origen, })