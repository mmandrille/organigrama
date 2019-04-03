from django.contrib import admin
#Importamos nuestros modelos
from .models import Organismo, Funcionario
# Register your models here.
class OrganismoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class FuncionarioAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos']

admin.site.register(Organismo, OrganismoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)