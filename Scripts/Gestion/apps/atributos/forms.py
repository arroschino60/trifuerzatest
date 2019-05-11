from django import forms

from apps.atributos.models import Atributo, Criterio

class atributoForm(forms.ModelForm):

    class Meta:
        model = Atributo
        fields = [
            'atributo',
        ]
        labels = {
            'atributo': 'Atributo',
        }
        widgets = {
            'atributo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class criterioForm(forms.ModelForm):
    class Meta:
        model = Criterio
        fields = [
            'criterio',
            'atributo',
        ]
        labels = {
            'criterio': 'Criterio',
             'atributo': 'Atributo',
        }
        widgets = {
            'criterio': forms.TextInput(attrs={'class': 'form-control'}),
            'atributo': forms.Select(attrs={'class': 'form-control'}),
        }