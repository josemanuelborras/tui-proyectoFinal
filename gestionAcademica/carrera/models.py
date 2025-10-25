from django.db import models

from materia.models import Materia

class CarrerasType(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class CarreraMateria(models.Model):
    carrera = models.ForeignKey('Carrera', on_delete=models.CASCADE)
    materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE)
    anio = models.PositiveIntegerField()
    cuatrimestre = models.PositiveIntegerField()

    class Meta:
        unique_together = ('carrera', 'materia')

    def __str__(self):
        return f"{self.carrera} - {self.materia} (Año {self.anio}, {self.cuatrimestre}° Cuatrimestre)"

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.ForeignKey(CarrerasType, on_delete=models.CASCADE, related_name='carreras', null=True, blank=True)
    materias = models.ManyToManyField(
        Materia,
        through='CarreraMateria',
        related_name='carreras'
    )

    def __str__(self):
        return self.nombre
