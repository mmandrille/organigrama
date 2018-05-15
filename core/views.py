from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, timedelta
#Import Personales
from .models import Organismo, Funcionario

# Create your views here.
def home(request):
    #Obtenemos todos los organismos
    origen = Organismo.objects.get(padre=None, activo=True)
    return render(request, 'home.html', {'origen': origen, })

def crear_sub_org(request, id_padre):
    new_org = Organismo()
    new_org.padre = Organismo.objects.get(pk=id_padre) 
    new_org.nombre = 'SubOrganismo'
    new_org.save()
    return HttpResponseRedirect('/admin/core/organismo/'+ str(new_org.id) + '/change/')