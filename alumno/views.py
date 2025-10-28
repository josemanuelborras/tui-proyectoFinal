from django.shortcuts import render,redirect, get_object_or_404
from .forms import AlumnoForm, InscripcionCarreraForm
from django.shortcuts import render, redirect
from .models import Alumno, InscripcionCarrera, InscripcionMateria
from .forms import AlumnoForm, InscripcionCarreraForm
from materia.models import Materia
from carrera.models import CarreraMateria

def inscripcion_carrera(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        carrera_form = InscripcionCarreraForm(request.POST)

        if alumno_form.is_valid() and carrera_form.is_valid():
            alumno = alumno_form.save()
            inscripcion_carrera = carrera_form.save(commit=False)
            inscripcion_carrera.alumno = alumno
            inscripcion_carrera.save()
            

            # Cargar materias asociadas a esa carrera
            materias = CarreraMateria.objects.filter(carrera=inscripcion_carrera.carrera)
            return render(request, 'alumno/inscripcion_materias.html', {
                'alumno': alumno,
                'carrera': inscripcion_carrera.carrera,
                'materias': materias,
            })
        
    else:
        alumno_form = AlumnoForm()
        carrera_form = InscripcionCarreraForm()

    return render(request, 'alumno/inscripcion_carrera.html', {
        'alumno_form': alumno_form,
        'carrera_form': carrera_form,
    })


def inscripcion_materias_view(request, alumno_id, carrera_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    carrera = get_object_or_404(Carrera, id=carrera_id)
    materias = CarreraMateria.objects.filter(carrera=carrera)

    if request.method == 'POST':
        materias_ids = request.POST.getlist('materias')
        inscripcion_carrera = InscripcionCarrera.objects.get(alumno=alumno, carrera=carrera)

        for materia_id in materias_ids:
            materia = Materia.objects.get(id=materia_id)
            InscripcionMateria.objects.create(
                inscripcion_carrera=inscripcion_carrera,
                materia=materia
            )

        return render(request, 'alumno/confirmacion.html', {
            'alumno': alumno,
            'carrera': carrera,
            'materias': Materia.objects.filter(id__in=materias_ids)
        })

    return render(request, 'alumno/inscripcion_materias.html', {
        'alumno': alumno,
        'carrera': carrera,
        'materias': materias
    })
