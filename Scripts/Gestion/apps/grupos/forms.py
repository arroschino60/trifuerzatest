from django import forms

from apps.grupos.models import Grupos

class grupoForm(forms.ModelForm):

    class Meta:
        model = Grupos
        fields = [
            #'grupo',
            'clave',
            'cantAlumnos',
            'profesor',
        ]
        labels = {
            #'grupo': '',
            'clave': '',
            'cantAlumnos': '',
            'profesor': '',
        }
        widgets = {
            #'grupo': forms.TextInput(attrs={'placeholder': 'Nombre del grupo'}),
            'clave': forms.TextInput(attrs={'placeholder': 'Clave del Grupo'}),
            'cantAlumnos': forms.TextInput(attrs={'placeholder': 'Cantidad de Alumnos'}),
            'profesor': forms.Select(attrs={'placeholder': 'Asignar Profesor'}),
        }