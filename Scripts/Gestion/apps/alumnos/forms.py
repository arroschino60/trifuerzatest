from django import forms

from apps.alumnos.models import Alumnos
from apps.carreras.models import Carrera, Especialidad

class FileForm(forms.Form):
    file = forms.FileField(
        label="Archivo",
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'custom-file-input',
                'accept': '.xls, .xlsx, .csv, .txt'
            }
        )
    )

class alumnoForm(forms.ModelForm):
    carrera = forms.ModelChoiceField(
        queryset=Carrera.objects.all(), empty_label="Seleccionar Carrera",
        required=True,
    )

    especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all(), empty_label="Seleccionar Especialidad",
        required=False,
    )

    class Meta:
        model = Alumnos
        fields = '__all__'
        """[
            'nControl',
            'nombre',
            'ap_Pat',
            'ap_Mat',
            'email',
            'password',
            'fechaIngreso',
            'carrera',
            'especialidad',
        ]"""
        # fields = '__all__'
        labels = {
            'nControl': '',
            'nombre': '',
            'ap_Pat': '',
            'ap_Mat': '',
            'email': '',
            'password': '',
            'fechaIngreso': '',
            'carrera': '',
            'especialidad': '',
        }
        widgets = {
            'nControl': forms.TextInput(attrs={'placeholder': 'Número de Control'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre(s)'}),
            'ap_Pat': forms.TextInput(attrs={'placeholder': 'Ap. Paterno'}),
            'ap_Mat': forms.TextInput(attrs={'placeholder': 'Ap. Materno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'fechaIngreso': forms.DateInput(attrs={'placeholder': 'Fecha de Ingreso', 'type': 'date'}),
            'carrera': forms.Select(attrs={'placeholder': 'Seleccione Carrera'}),
            'especialidad': forms.Select(attrs={'placeholder': 'Seleccione Especialidad'}),
        }