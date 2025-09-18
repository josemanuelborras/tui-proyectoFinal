from django.shortcuts import render, redirect, get_object_or_404

from .models import CarrerasType
from adminPanel.models import Admin
from .carrerasTypeForm import CarrerasTypeForm
from carrera.models import Carrera
from .carreraForm import CarreraForm

# listado de tipos de carreras
def carreras_type(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    tipos_carrera = CarrerasType.objects.all().order_by('id')

    if request.method == 'POST':
        form = CarrerasTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carreras_type')
    else:
        form = CarrerasTypeForm()

    return render(request, 'adminPanel/carreras_type.html', {
        'tipos_carrera': tipos_carrera,
        'usuario_logueado': admin.usuario,
        'form': form
    })

# eliminar tipo de carrera
def carreras_type_delete(request, id):
    if request.method == 'POST':
        tipo = get_object_or_404(CarrerasType, id=id)
        tipo.delete()
    return redirect('carreras_type')

# editar tipo de carrera
def carreras_type_edit(request, id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    tipo = get_object_or_404(CarrerasType, id=id)
    tipos_carrera = CarrerasType.objects.all().order_by('id')

    if request.method == 'POST':
        edit_form = CarrerasTypeForm(request.POST, instance=tipo)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('carreras_type')
        
        form = CarrerasTypeForm() 
        return render(request, 'adminPanel/carreras_type.html', {
            'tipos_carrera': tipos_carrera,
            'usuario_logueado': admin.usuario,
            'form': form,
            'edit_form': edit_form,
            'edit_id': id,
        })
    else:
        return redirect('carreras_type')

# listado de carreras
def carreras_list(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    carreras = Carrera.objects.all()
    admin = Admin.objects.get(id=request.session['admin_id'])
    form = CarreraForm()
    tipos_carrera = CarrerasType.objects.all()
    return render(request, 'adminPanel/carreras_list.html', {
        'carreras': carreras,
        'usuario_logueado': admin.usuario,
        'form': form,
        'tipos_carrera': tipos_carrera
    })

# crear nueva carrera
def carrera_create(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    tipos_carrera = CarrerasType.objects.all()
    if not tipos_carrera.exists():
        return render(request, 'adminPanel/carrera_create.html', {
            'error': 'Debe crear al menos un Tipo de Carrera antes de crear una Carrera.',
            'usuario_logueado': admin.usuario
        })
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carreras_list')
    else:
        form = CarreraForm()
    return render(request, 'adminPanel/carrera_create.html', {
        'form': form,
        'usuario_logueado': admin.usuario
    })

# editar carrera
def carrera_edit(request, id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    carrera = get_object_or_404(Carrera, id=id)
    tipos_carrera = CarrerasType.objects.all()
    if request.method == 'POST':
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('carreras_list')
    else:
        form = CarreraForm(instance=carrera)
    return render(request, 'adminPanel/carrera_edit.html', {
        'form': form,
        'usuario_logueado': admin.usuario,
        'carrera': carrera,
        'tipos_carrera': tipos_carrera
    })

# eliminar carrera
def carrera_delete(request, id):
    if request.method == 'POST':
        carrera = get_object_or_404(Carrera, id=id)
        carrera.delete()
    return redirect('carreras_list')