from django.shortcuts import render, redirect
from .login import LoginForm
from .models import Admin

# import de carreras
from carrera.models import Carrera

def login_view(request):
    if request.session.get('admin_id'):
        return redirect('admin_home')
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            try:
                admin = Admin.objects.get(usuario=usuario, password=password)
                request.session['admin_id'] = admin.id
                return redirect('admin_home')
            except Admin.DoesNotExist:
                error = "Usuario o contraseña incorrectos"
    else:
        form = LoginForm()
    return render(request, 'adminPanel/login.html', {'form': form, 'error': error})

def admin_home(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    return render(request, 'adminPanel/home.html')

def logout_view(request):
    request.session.flush()
    return redirect('admin_login')

# listado de carreras
def carreras_list(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    carreras = Carrera.objects.all()
    return render(request, 'adminPanel/carreras_list.html', {'carreras': carreras})