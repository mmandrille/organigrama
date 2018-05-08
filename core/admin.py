from django.contrib import admin
#Importamos nuestros modelos
from .models import Organismo, Funcionario
# Register your models here.
admin.site.register(Organismo)
admin.site.register(Funcionario)