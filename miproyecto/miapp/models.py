from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=45,verbose_name='Ingrese Nombre del Alumno')
    apellido = models.CharField(max_length=45,verbose_name='Ingrese Apellido del Alumno')
    edad = models.IntegerField(verbose_name='Ingreses edad del Alumno')
    email = models.EmailField(verbose_name='Ingrese Correo del Alumno')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'