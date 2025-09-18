from django import forms
from .models import Carrera, CarrerasType

class CarreraForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(
        queryset=CarrerasType.objects.all(),
        empty_label="Elegir un tipo de carrera"
    )

    class Meta:
        model = Carrera
        fields = ['nombre', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la carrera'}),
        }