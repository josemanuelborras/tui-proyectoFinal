from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Alumno, AlumnoCarrera, AlumnoMateria
from carrera.models import Carrera, CarreraMateria
from adminPanel.models import Admin
from .alumnosForm import AlumnosForm
from materia.models import Materia

from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa


def alumnos_list(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    alumnos = Alumno.objects.all().order_by('apellido', 'nombre')
    form = AlumnosForm()
    
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.password = form.cleaned_data['dni']
            alumno = form.save()
            messages.success(request, f'Alumno {alumno.nombre} {alumno.apellido} registrado exitosamente.')
            return redirect('alumnos_list')
    
    return render(request, 'adminPanel/alumnos_list.html', {
        'alumnos': alumnos,
        'form': form,
        'usuario_logueado': admin.usuario
    })

def alumno_delete(request, alumno_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    alumno = get_object_or_404(Alumno, id=alumno_id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnos_list')
    # Si quieres, puedes mostrar una confirmación antes de borrar
    return redirect('alumnos_list')

def alumno_detail(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    carreras_inscripto = AlumnoCarrera.objects.filter(alumno=alumno)
    carreras = Carrera.objects.all()
    return render(request, 'adminPanel/alumno_detail.html', {
        'alumno': alumno,
        'carreras': carreras,
        'carreras_inscripto': carreras_inscripto,
    })

def alumno_inscribir_carrera(request, alumno_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    alumno = get_object_or_404(Alumno, id=alumno_id)
    if request.method == 'POST':
        carrera_id = request.POST.get('carrera_id')
        if carrera_id:
            carrera = get_object_or_404(Carrera, id=carrera_id)
            # Evita inscribir dos veces en la misma carrera
            if not AlumnoCarrera.objects.filter(alumno=alumno, carrera=carrera).exists():
                AlumnoCarrera.objects.create(alumno=alumno, carrera=carrera)
        return redirect('alumno_detail', alumno_id=alumno_id)
    return redirect('alumno_detail', alumno_id=alumno_id)

def alumno_comprobante(request, alumno_id, carrera_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    carrera = get_object_or_404(Carrera, id=carrera_id)
    inscripcion = get_object_or_404(AlumnoCarrera, alumno=alumno, carrera=carrera)

    html = render_to_string('adminPanel/comprobante_inscripcion_carrera.html', {
        'alumno': alumno,
        'carrera': carrera,
        'inscripcion': inscripcion,
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=comprobante_{alumno.dni}_{carrera.nombre}.pdf'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response

def alumno_login(request):
    error = None
    if request.method == 'POST':
        dni = request.POST.get('dni')
        password = request.POST.get('password')
        try:
            alumno = Alumno.objects.get(dni=dni, password=password)
            request.session['alumno_id'] = alumno.id
            return redirect('alumno_panel')
        except Alumno.DoesNotExist:
            error = "DNI o contraseña incorrectos."
    return render(request, 'alumnosPanel/alumno_login.html', {'error': error})

def alumno_panel(request):
    alumno_id = request.session.get('alumno_id')
    if not alumno_id:
        return redirect('alumno_login')
    alumno = get_object_or_404(Alumno, id=alumno_id)
    carreras_inscripto = AlumnoCarrera.objects.filter(alumno=alumno)
    return render(request, 'alumnosPanel/alumno_panel.html', {'alumno': alumno, 'carreras_inscripto': carreras_inscripto})

def alumno_carrera_detail(request, carrera_id):
    alumno_id = request.session.get('alumno_id')
    if not alumno_id:
        return redirect('alumno_login')
    carrera = get_object_or_404(Carrera, id=carrera_id)
    alumno = get_object_or_404(Alumno, id=alumno_id)
    materias = CarreraMateria.objects.filter(carrera=carrera).order_by('anio', 'cuatrimestre')
    materias_inscriptas = AlumnoMateria.objects.filter(alumno=alumno, carrera=carrera)
    materias_estado = {am.materia.id: am for am in materias_inscriptas}
    return render(request, 'alumnosPanel/carrera_detail.html', {
        'carrera': carrera,
        'materias': materias,
        'materias_estado': materias_estado,
    })

def alumno_inscribir_materia(request, carrera_id, materia_id):
    alumno_id = request.session.get('alumno_id')
    if not alumno_id:
        return redirect('alumno_login')
    alumno = get_object_or_404(Alumno, id=alumno_id)
    carrera = get_object_or_404(Carrera, id=carrera_id)
    materia = get_object_or_404(Materia, id=materia_id)

    # Verifica que el alumno esté inscripto en la carrera
    if not AlumnoCarrera.objects.filter(alumno=alumno, carrera=carrera).exists():
        return redirect('alumno_panel')

    # Evita inscripciones duplicadas
    if not AlumnoMateria.objects.filter(alumno=alumno, materia=materia, carrera=carrera).exists():
        AlumnoMateria.objects.create(alumno=alumno, materia=materia, carrera=carrera)

    return redirect('alumno_carrera_detail', carrera_id=carrera_id)

def alumno_comprobante_materia(request, carrera_id, materia_id):
    alumno_id = request.session.get('alumno_id')
    if not alumno_id:
        return redirect('alumno_login')
    alumno = get_object_or_404(Alumno, id=alumno_id)
    carrera = get_object_or_404(Carrera, id=carrera_id)
    materia = get_object_or_404(Materia, id=materia_id)
    inscripcion = get_object_or_404(AlumnoMateria, alumno=alumno, carrera=carrera, materia=materia)

    html = render_to_string('alumnosPanel/comprobante_materia.html', {
        'alumno': alumno,
        'carrera': carrera,
        'materia': materia,
        'inscripcion': inscripcion,
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=comprobante_{alumno.dni}_{materia.nombre}.pdf'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response

def alumno_logout(request):
    request.session.pop('alumno_id', None)
    return redirect('alumno_login')