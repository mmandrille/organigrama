import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, timedelta
from django.core import serializers
from django.views.generic import View
from django.utils import timezone

#Import Personales
from .models import Organismo, Funcionario
from .render import Custom_render


# Create your views here.
def home(request, origen_id=None):
    if origen_id is None:
        origen = Organismo.objects.filter(padre=None, activo=True).order_by('id').first()
    else:
        origen = Organismo.objects.get(id=origen_id, activo=True)
    return render(request, 'home.html', {'origen': origen, })

def home_limit(request, padre_id, max_child):
    origen = Organismo.objects.get(id=padre_id)
    return render(request, 'home_limit.html', {'origen': origen, 'max_child': max_child})

def home_listado(request, editable=None):
    origen = Organismo.objects.filter(padre=None, activo=True).order_by('id').first()
    fecha = timezone.now()
    return render(request, 'pdf/lista_pdf.html', {'origen': origen, 'editable': editable, 'fecha': fecha, })

def home_pdf(request, origen_id=None):
    if origen_id is None:
        origen = Organismo.objects.filter(padre=None, activo=True).order_by('id').first()
    else:
        origen = Organismo.objects.get(id=origen_id, activo=True)
    today = timezone.now()
    params = {
        'today': today,
        'request': request,
        'origen' : origen,
    }
    return Custom_render.pdf('pdf/lista_pdf.html', params)

def crear_sub_org(request, id_padre):
    new_org = Organismo()
    new_org.padre = Organismo.objects.get(pk=id_padre)
    new_org.nombre = 'SubOrganismo'
    new_org.save()
    return HttpResponseRedirect('/admin/core/organismo/'+ str(new_org.id) + '/change/')

def ws_org(request):
    organismos = [org.as_dict() for org in Organismo.objects.filter(activo=True)]
    return HttpResponse(json.dumps({"data": organismos}), content_type='application/json')

def ws_org_max(request, padre_id, max_child):
    organismos = Organismo.objects.none()
    org_buscar = Organismo.objects.filter(id=padre_id)

    for x in range(max_child):
        organismos = organismos | org_buscar
        for org in org_buscar:
            org_buscar = org_buscar.exclude(id=org.id)
            org_buscar = org_buscar | Organismo.objects.filter(padre=org)

    organismos = organismos | org_buscar
    organismos = [org.as_dict() for org in organismos]#Lo convertimos en diccionario serialiable
    return HttpResponse(json.dumps({"data": organismos}), content_type='application/json')

def ws_func(request):
    funcionarios = [func.as_dict() for func in Funcionario.objects.filter(activo=True)]
    return HttpResponse(json.dumps({"data": funcionarios}), content_type='application/json')