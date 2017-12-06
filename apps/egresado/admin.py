from django.contrib import admin
from apps.egresado.models import Interes, Sexo, Pais, Departamento, Carrera, Egresado

# Register your models here.

admin.site.register(Interes)
admin.site.register(Sexo)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Carrera)
admin.site.register(Egresado)