from django.db import models
from carrera.models import Carrera, CarreraMateria
from materia.models import Materia

class Alumno(models.Model):
    dni = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class InscripcionCarrera(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} - {self.carrera}"


class InscripcionMateria(models.Model):
    inscripcion_carrera = models.ForeignKey(InscripcionCarrera, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.inscripcion_carrera.alumno} - {self.materia}"
