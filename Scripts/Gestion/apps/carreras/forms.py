from django import forms

from apps.carreras.models import Carrera, Especialidad
#from apps.especialidades.models import

class FileFormCarrera(forms.Form):
    file = forms.FileField(
        label="Carreras",
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'custom-file-input',
                'accept': '.xls, .xlsx, .csv, .txt'
            }
        )
    )

class FileFormEspecialidad(forms.Form):
    file = forms.FileField(
        label="Especialidades",
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'custom-file-input',
                'accept': '.xls, .xlsx, .csv, .txt'
            }
        )
    )
class carreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = [
            'carrera',
            'clave',
            'color',
        ]
        labels = {
            'carrera': '',
            'clave': '',
            'color': '',
        }
        widgets = {
            'carrera': forms.TextInput(attrs={'placeholder': 'Nombre de la Carrera'}),
            'clave': forms.TextInput(attrs={'placeholder': 'Clave de la Carrera'}),
            'color': forms.TextInput(attrs={'placeholder': 'Selecciona un color', 'id': 'Color'}),
        }

class especialidadForm(forms.ModelForm):

    class Meta:
        model = Especialidad
        fields = [
            'especialidad',
            'clave',
            'color',
            'planEstudios',
        ]
        labels = {
            'especialidad': '',
            'clave': '',
            'color': '',
            'planEstudios': '',
        }
        widgets = {
            'especialidad': forms.TextInput(attrs={'placeholder': 'Nombre de la Especialidad'}),
            'clave': forms.TextInput(attrs={'placeholder': 'Clave de la Especialidad'}),
            'color': forms.TextInput(attrs={'placeholder': 'Color de la Especialidad', 'id': 'Color'}),
            'planEstudios': forms.TextInput(attrs={'placeholder': 'Plan de Estudios'}),
        }

