from django.contrib import admin
#Importamos nuestros modelos
from .models import Organismo, Funcionario
# Register your models here.
class FuncionarioInline(admin.TabularInline):
    model = Funcionario

class OrganismoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    inlines = [FuncionarioInline]
    raw_id_fields = ("padre",)
    list_filter = ['jerarquia',]

class FuncionarioAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos']
    raw_id_fields = ("organismo",)

admin.site.register(Organismo, OrganismoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)