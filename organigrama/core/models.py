from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.core.files.storage import FileSystemStorage

from datetime import datetime, date
#Import personales
from organigrama.settings import MEDIA_URL

#Choice Field
JERARQUIA = ((0, 'Sin Jerarquia'),
            (10, 'Poder Gubernamental'),
            (20, 'Gobernacion'),
            (30, 'Ministerio'),(31, 'Secretaria'),(32, 'SubSecretaria'),(33, 'Direccion'),(34, 'Coordinacion'),
            (40, 'Legislativo'),
            (50, 'Judicial'),
            (60, 'Municipio'),(61, 'Intendencia'),(62, 'Consejo'),
            (70, 'Escleciastico'),
            (80, 'Privados'),
            )

CARGOS =    ((0, 'Sin Cargo'),
            (1, 'Gobernador'), (2, 'Vice Gobernador'),
            (10, 'Ministro'),
            (20, 'Secretario'), (21, 'Secretaria'), (22, 'Subsecretario'), (23, 'SubScretaria'),
            (31, 'Director'), (32, 'Directora'), (33, 'SubDirector'), (34, 'SubDirectora'), 
            (41, 'Coordinador'), (42, 'Coordinadora'),
            (51, 'Consejal'), (52, 'Diputado'), (53, 'Senador'), (54, 'Diputada'), (55, 'Senadora'),
            (61, 'Juez'), (62, 'Fiscal'), (63, 'Vocal'), (64, 'Procurador'), (65, 'Procuradora'), (66, 'Defensor'),
            (71, 'Intendente'), (72, 'Comisionado'),
            (81, 'Escribano'), (82, 'Presidente'), (83, 'Vice Presidente'),
            (91, 'Administrativo'), (92, 'Jefe'), (93, 'Obispo'), (94, 'Sacerdote'), (95, 'Parroco'), (97, 'Consul'), (99, 'Asesor'))

# Create your models here.
class Organismo(models.Model):
    padre = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='hijos')
    nombre = models.CharField('Titulo', max_length=200)
    jerarquia = models.IntegerField(choices=JERARQUIA, default=0)
    descripcion = HTMLField(blank=True, null=True)
    icono = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=200, blank=True, null=True)
    cuit = models.CharField('CUIT', max_length=13, blank=True, null=True)
    telefonos = models.CharField('Telefonos', max_length=100, blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    color = models.CharField(max_length=7, default="#ffffff")
    activo = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    def __str__(self):
        if self.padre is not None:
            return self.nombre + ' > ' + self.padre.nombre
        else:
            return self.nombre + ' (Sin Asignar)'
    def as_dict(self):
        if self.padre is None:
            self.padre = self
        return {
            "id": self.id,
            "nombre": self.nombre,
            "padre": self.padre.id,
        }
    def funcionario_actual(self):
        return self.funcionarios.filter(activo=True)

class Funcionario(models.Model):
    organismo = models.ForeignKey(Organismo, on_delete=models.SET_NULL, related_name='funcionarios', blank=True, null=True)
    cargo = models.IntegerField(choices=CARGOS, default=0)
    subcargo = models.CharField('SubCargo', max_length=20, blank=True, null=True)
    funcion_unica = models.BooleanField(default=False)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    foto = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), blank=True, null=True)
    dni = models.CharField('DNI', max_length=100, blank=True, null=True)
    titulo = models.CharField('Titulo Profesional', max_length=20)
    email = models.EmailField('Correo Personal', blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    decreto = models.IntegerField(blank=True, null=True)
    begda = models.DateField('Designacion',  default=date(2019, 1, 1))
    endda = models.DateField('Cese de Funciones', default=date(9999, 12, 31))
    activo = models.BooleanField(default=True)
    def __str__(self):
        if self.organismo is None: 
            return 'Sin Organismo > ' + self.nombres + ' ' + self.apellidos
        else:
            return self.organismo.nombre + ' > ' + self.nombres + ' ' + self.apellidos
    def as_dict(self):
        return {
            "organismo": self.organismo.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "cargo": dict(CARGOS).get(self.cargo),
            "dni": self.dni,
        }
    def save(self, *args, **kwargs):
        if self.activo == True and self.funcion_unica:#tener en cuenta otros funcionarios
            self.organismo.funcionarios.exclude(pk=self.pk).filter(cargo=self.cargo,subcargo=self.subcargo).update(endda=self.begda, activo=False)
        super(Funcionario, self).save(*args, **kwargs)
