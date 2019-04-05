from django.contrib import admin
#Importamos nuestros modelos
from .models import Organismo, Funcionario
# Register your models here.
class FuncionarioInline(admin.TabularInline):
    model = Funcionario

class OrganismoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    inlines = [FuncionarioInline]

class FuncionarioAdmin(admin.ModelAdmin):
    raw_id_fields = ("organismo",)
    search_fields = ['nombres', 'apellidos']

admin.site.register(Organismo, OrganismoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)