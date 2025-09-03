from django.shortcuts import render, redirect
from .login import LoginForm
from .models import Admin

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
