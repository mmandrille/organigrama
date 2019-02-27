import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, timedelta
from django.core import serializers

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

def ws_org(request):
    organismos = [org.as_dict() for org in Organismo.objects.filter(activo=True)]
    return HttpResponse(json.dumps({"data": organismos}), content_type='application/json')

def ws_func(request):
    funcionarios = [func.as_dict() for func in Funcionario.objects.filter(activo=True)]
    return HttpResponse(json.dumps({"data": funcionarios}), content_type='application/json')