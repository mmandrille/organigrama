from __future__ import unicode_literals
import datetime

from django.db import models
from tinymce.models import HTMLField
from django.core.files.storage import FileSystemStorage

#Import personales
from organigrama.settings import MEDIA_URL

#Choice Field
CARGOS =    ((0,'Gobernador'), 
            (10,'Secretario'), (11, 'Secretaria'),
            (21, 'Director'), (22, 'Directora'), 
            (31, 'Coordinador'), (32, 'Coordinadora'),

            (99, 'Administrativo'))

# Create your models here.
class Organismo(models.Model):
    padre = models.OneToOneField('self', on_delete=models.CASCADE)
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = HTMLField()
    icono = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), null=True)
    direccion = models.CharField('Direccion', max_length=200)
    cuit = models.CharField('CUIT', max_length=13)
    telefonos = models.CharField('Telefonos', max_length=100)
    web = models.URLField('Web')

class Funcionario(models.Model):
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE)
    cargo = harField(max_length=2,choices=CARGOS, default=99)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    dni = models.CharField('DNI', max_length=100)
    titulo = models.CharField('Titulo Profesional', max_length=20)
    email = models.EmailField()
    telefono = models.CharField('Telefono', max_length=20)
    activo = models.BooleanField(default=True)