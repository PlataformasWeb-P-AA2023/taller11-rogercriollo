from django.contrib import admin
from django.contrib import admin
from taller011.models import Departamento, Edificio


class EdificioAdmin(admin.ModelAdmin):
   
    list_display = ('nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'tipo')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
 
    list_display = ('Departamento', 'costo', 'num_cuartos', 'edificio', )
  
    raw_id_fields = ('Departamento',)

admin.site.register(Departamento, DepartamentoAdmin)
