from django import forms

from apps.carreras.models import Carrera, Especialidad
#from apps.especialidades.models import

class carreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = [
            'carrera',
            'clave',
            'color',
        ]
        labels = {
            'carrera': 'Carrera',
            'clave': 'Clave',
            'color': 'Color',
        }
        widgets = {
            'carrera': forms.TextInput(attrs={'class':'form-control'}),
            'clave': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
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
            'especialidad': 'Especialidad',
            'clave': 'Clave',
            'color': 'Color',
            'planEstudios': 'Plan de Estudios',
        }
        widgets = {
            'especialidad': forms.TextInput(attrs={'class':'form-control'}),
            'clave': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'planEstudios': forms.TextInput(attrs={'class': 'form-control'}),
        }

