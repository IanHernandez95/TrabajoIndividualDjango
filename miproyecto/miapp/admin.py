from django.contrib import admin
from . import models

# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido',)

admin.site.register(models.Alumno, AlumnoAdmin)


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_contratacion',)
    list_filter=('fecha_contratacion',)


admin.site.register(models.Profesor, ProfesorAdmin)