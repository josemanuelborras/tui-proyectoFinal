from django import forms
from .models import Materia

class MateriasForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la materia',
                'class': 'input',
            }),
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
                'unique': 'Ya existe una materia con ese nombre.',
                'max_length': 'El nombre es demasiado largo.',
            },
        }