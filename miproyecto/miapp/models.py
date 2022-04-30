from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=45,)
    apellido = models.CharField(max_length=45,)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=45,)
    apellido = models.CharField(max_length=45,)
    edad = models.IntegerField()
    email = models.EmailField()
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'