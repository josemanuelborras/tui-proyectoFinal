from django import forms
from .models import Alumno, InscripcionCarrera, InscripcionMateria
from carrera.models import Carrera
from materia.models import Materia

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'apellido', 'email']


class InscripcionCarreraForm(forms.ModelForm):
    class Meta:
        model = InscripcionCarrera
        fields = ['carrera']


class InscripcionMateriaForm(forms.ModelForm):
    materias = forms.ModelMultipleChoiceField(
        queryset=Materia.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = InscripcionMateria
        fields = ['materias']
