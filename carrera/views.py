from django.shortcuts import render, redirect, get_object_or_404

from .models import CarrerasType
from adminPanel.models import Admin
from .carrerasTypeForm import CarrerasTypeForm
from .models import Carrera
from .carreraForm import CarreraForm
from .models import CarreraMateria
from materia.models import Materia

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

# detalle de carrera
def carrera_detail(request, carrera_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    carrera = get_object_or_404(Carrera, id=carrera_id)

    carrera_materias = CarreraMateria.objects.filter(carrera=carrera).order_by('anio', 'cuatrimestre')

    materias_existentes = CarreraMateria.objects.filter(carrera=carrera).values_list('materia_id', flat=True)
    materias_disponibles = Materia.objects.exclude(id__in=materias_existentes)
    
    return render(request, 'adminPanel/carrera_detail.html', {
        'carrera': carrera,
        'carrera_materias': carrera_materias,
        'materias_disponibles': materias_disponibles,
        'usuario_logueado': admin.usuario
    })

def carrera_agregar_materia(request, carrera_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    
    if request.method == 'POST':
        carrera = get_object_or_404(Carrera, id=carrera_id)
        materia_id = request.POST.get('materia_id')
        cuatrimestre = request.POST.get('cuatrimestre')
        anio = request.POST.get('anio')
        
        materia = get_object_or_404(Materia, id=materia_id)
        
        # Verificar que no exista ya la relación
        if not CarreraMateria.objects.filter(carrera=carrera, materia=materia).exists():
            CarreraMateria.objects.create(
                carrera=carrera,
                materia=materia,
                cuatrimestre=cuatrimestre,
                anio=anio
            )
    
    return redirect('carrera_detail', carrera_id=carrera_id)

def carrera_quitar_materia(request, carrera_id, materia_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    
    if request.method == 'POST':
        carrera_materia = get_object_or_404(
            CarreraMateria, 
            carrera_id=carrera_id, 
            materia_id=materia_id
        )
        carrera_materia.delete()
    
    return redirect('carrera_detail', carrera_id=carrera_id)