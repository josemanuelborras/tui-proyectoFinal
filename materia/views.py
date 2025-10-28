from django.shortcuts import render, redirect, get_object_or_404

from adminPanel.models import Admin
from .models import Materia
from .materiasForm import MateriasForm

# Eliminar materia
def materia_delete(request, materia_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    materia = get_object_or_404(Materia, id=materia_id)
    if request.method == 'POST':
        materia.delete()
        return redirect('materias_list')
    
# Editar materia
def materia_edit(request, materia_id):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    materia = get_object_or_404(Materia, id=materia_id)
    if request.method == 'POST':
        form = MateriasForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materias_list')
    else:
        form = MateriasForm(instance=materia)
    return render(request, 'adminPanel/materia_edit.html', {
        'form': form,
        'materia': materia,
        'usuario_logueado': admin.usuario
    })

# Create your views here.
# listado de materias
def materias_list(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    materias = Materia.objects.all().order_by('id')
    form = MateriasForm()
    return render(request, 'adminPanel/materias_list.html', {
        'materias': materias,
        'usuario_logueado': admin.usuario,
        'form': form
    })

# crear nueva materia
def materia_create(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    admin = Admin.objects.get(id=request.session['admin_id'])
    if request.method == 'POST':
        form = MateriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materias_list')
    else:
        form = MateriasForm()
    return render(request, 'adminPanel/materia_create.html', {
        'form': form,
        'usuario_logueado': admin.usuario
    })