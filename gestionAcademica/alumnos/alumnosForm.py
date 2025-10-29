from django import forms
from .models import Alumno
from carrera.models import Carrera

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'email', 'telefono', 'fecha_nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del alumno'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido del alumno'
            }),
            'dni': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'DNI (8 dígitos)',
                'maxlength': '8'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@ejemplo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono (opcional)'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'DNI',
            'email': 'Email',
            'telefono': 'Teléfono',
            'fecha_nacimiento': 'Fecha de Nacimiento'
        }

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if not dni.isdigit():
            raise forms.ValidationError("El DNI debe contener solo números.")
        if len(dni) != 8:
            raise forms.ValidationError("El DNI debe tener exactamente 8 dígitos.")
        return dni

    def clean_email(self):
        email = self.cleaned_data['email']
        # Verificar que el email no esté ya registrado
        if Alumno.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un alumno con este email.")
        return email
