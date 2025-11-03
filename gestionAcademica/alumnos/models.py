from django.db import models

from carrera.models import Carrera
from materia.models import Materia

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    fecha_nacimiento = models.DateField()
    
    # Relación muchos a muchos con Carrera
    carreras = models.ManyToManyField(
        Carrera, 
        through='AlumnoCarrera', 
        related_name='alumnos'
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.dni}"

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ['apellido', 'nombre']

class AlumnoCarrera(models.Model):
    """Tabla intermedia para inscripción de alumno en carrera"""
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('alumno', 'carrera')

    def __str__(self):
        return f"{self.alumno} - {self.carrera}"

class AlumnoMateria(models.Model):
    """Tabla de inscripciones de alumno en materias"""
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[
        ('inscripto', 'Inscripto'),
        ('cursando', 'Cursando'),
        ('aprobado', 'Aprobado'),
        ('reprobado', 'Reprobado'),
        ('abandonado', 'Abandonado'),
    ], default='inscripto')
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('alumno', 'materia', 'carrera')

    def __str__(self):
        return f"{self.alumno} - {self.materia} ({self.carrera})"