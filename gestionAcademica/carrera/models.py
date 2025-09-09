from django.db import models

class CarrerasType(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(CarrerasType, on_delete=models.CASCADE, related_name='carreras', null=True, blank=True)

    def __str__(self):
        return self.nombre
