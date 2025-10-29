from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Alumno, AlumnoCarrera, AlumnoMateria
from carrera.models import Carrera, CarreraMateria
from adminPanel.models import Admin
from .alumnosForm import AlumnosForm

def alumnos_list(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    alumnos = Alumno.objects.all().order_by('apellido', 'nombre')
    form = AlumnosForm()
    
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            messages.success(request, f'Alumno {alumno.nombre} {alumno.apellido} registrado exitosamente.')
            return redirect('alumnos_list')
    
    return render(request, 'adminPanel/partials/alumnos_main.html', {
        'alumnos': alumnos,
        'form': form,
        'usuario_logueado': admin.usuario
    })
