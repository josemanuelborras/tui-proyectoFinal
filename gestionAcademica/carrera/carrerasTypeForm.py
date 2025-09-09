from django import forms
from carrera.models import CarrerasType

class CarrerasTypeForm(forms.ModelForm):
    class Meta:
        model = CarrerasType
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese un nombre',
                'class': 'input',
            }),
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
                'unique': 'Ya existe un Tipo de Carrera con ese nombre.',
                'max_length': 'El nombre es demasiado largo.',
            },
        }