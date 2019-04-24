from django.contrib import admin
#Import Personales
from .form import OrganismoForm
from .models import Organismo, Funcionario

#Particularidades
class FuncionarioInline(admin.TabularInline):
    model = Funcionario

class OrganismoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    inlines = [FuncionarioInline]
    raw_id_fields = ("padre",)
    list_filter = ['jerarquia',]
    form = OrganismoForm

class FuncionarioAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos']
    raw_id_fields = ("organismo",)

# Register your models here.
admin.site.register(Organismo, OrganismoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)