from django.shortcuts import render, redirect, get_object_or_404

from .models import CarrerasType
from adminPanel.models import Admin
from .carrerasTypeForm import CarrerasTypeForm
from carrera.models import Carrera

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


def carreras_type_delete(request, id):
    if request.method == 'POST':
        tipo = get_object_or_404(CarrerasType, id=id)
        tipo.delete()
    return redirect('carreras_type')

# listado de carreras
def carreras_list(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    carreras = Carrera.objects.all()
    admin = Admin.objects.get(id=request.session['admin_id'])
    return render(request, 'adminPanel/carreras_list.html', {
        'carreras': carreras,
        'usuario_logueado': admin.usuario
    })
