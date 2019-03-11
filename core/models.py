from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.core.files.storage import FileSystemStorage

from datetime import datetime, date
#Import personales
from organigrama.settings import MEDIA_URL

#Choice Field
CARGOS =    ((0,'Gobernador'), (1,'Vice Gobernador'),
            (10,'Ministro'),
            (20,'Secretario'), (21, 'Secretaria'), (22, 'Subsecretario'), (23, 'SubScretaria'),
            (31, 'Director'), (32, 'Directora'), (33, 'SubDirector'), (34, 'SubDirectora'), 
            (41, 'Coordinador'), (42, 'Coordinadora'),
            (51, 'Consejal'), (52, 'Diputado'), (53, 'Senador'),
            (61, 'Juez'), (62, 'Fiscal'), (63, 'Vocal'),
            (71, 'Intendente'), (72, 'Comisionado'),
            (81, 'Escribano'), (82, 'Presidente'), (83, 'Vice Presidente'),
            (91, 'Administrativo'), (92, 'Jefe'), (93, 'Obispo'), (94, 'Sacerdote'), (95, 'Consul'), (96, 'Asesor'))

# Create your models here.
class Organismo(models.Model):
    padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='hijos')
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = HTMLField(blank=True, null=True)
    icono = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=200)
    cuit = models.CharField('CUIT', max_length=13, blank=True, null=True)
    telefonos = models.CharField('Telefonos', max_length=100)
    web = models.URLField('Web', blank=True, null=True)
    activo = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    def __str__(self):
        if self.padre is not None:
            return self.nombre + ' > ' + self.padre.nombre
        else:
            return self.nombre
    def as_dict(self):
        if self.padre is None:
            self.padre = self
        return {
            "id": self.id,
            "nombre": self.nombre,
            "padre": self.padre.id,
        }
    def funcionario_actual(self):
        return self.funcionarios.filter(activo=True).first()

class Funcionario(models.Model):
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, related_name='funcionarios')
    cargo = models.IntegerField(choices=CARGOS, default=99)
    funcion_unica = models.BooleanField(default=True)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    foto = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), blank=True, null=True)
    dni = models.CharField('DNI', max_length=100, blank=True, null=True)
    titulo = models.CharField('Titulo Profesional', max_length=20)
    email = models.EmailField('Correo Personal', blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    begda = models.DateField('Designacion', default=datetime.now)
    endda = models.DateField('Cese de Funciones', default=date(9999, 12, 31))
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.get_cargo_display() + ' de ' + self.organismo.nombre + '-' + self.nombres + ' ' + self.apellidos
    def as_dict(self):
        return {
            "organismo": self.organismo.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "cargo": dict(CARGOS).get(self.cargo),
            "dni": self.dni,
        }
    def save(self, *args, **kwargs):
        print("Super guardado")
        if self.funcion_unica:
            self.organismo.funcionarios.exclude(pk=self.pk).filter(endda=self.endda).update(endda=self.begda, activo=False)
        super(Funcionario, self).save(*args, **kwargs)