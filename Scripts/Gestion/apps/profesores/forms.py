from django import forms

from apps.profesores.models import Profesores

class profesorForm(forms.ModelForm):

    class Meta:
        model = Profesores
        fields = [
            'nombre',
            'ap_Pat',
            'ap_Mat',
            'email',
            'password',
            'rol',
        ]
        labels = {
            'nombre': '',
            'ap_Pat': '',
            'ap_Mat': '',
            'email': '',
            'password': '',
            'rol': '',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre(s)'}),
            'ap_Pat': forms.TextInput(attrs={'placeholder':'Ap. Paterno'}),
            'ap_Mat': forms.TextInput(attrs={'placeholder':'Ap. Materno'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Contraseña'}),
            'rol': forms.Select(attrs={'placeholder':'Tipo de Usuario'}),
        }