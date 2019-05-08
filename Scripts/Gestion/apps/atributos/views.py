from django.shortcuts import render
from apps.atributos.forms import atributoForm,criterioForm
from apps.atributos.models import Atributo, Criterio
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

# Create your views here.

class mostrarAtributos(ListView):
    model = Atributo
    template_name = 'atributos/index.html'

class registrarAtributo(CreateView):
    model = Atributo
    form_class = atributoForm
    template_name = 'atributos/registrarAtributo.html'
    success_url = reverse_lazy('atributos')

class atributoUpdate(UpdateView):
    model = Atributo
    form_class = atributoForm
    template_name = 'atributos/editar'
    success_url = reverse_lazy('atributos')

class atributoDelete(DeleteView):
    model = Atributo
    template_name = 'atributos/eliminar'
    success_url = reverse_lazy('atributos')

class registrarCriterio(CreateView):
    model = Criterio
    form_class = criterioForm
    template_name = 'atributos/criterio.html'
    success_url = reverse_lazy('atributos')
