from django.shortcuts import render
from apps.profesores.forms import profesorForm
from apps.profesores.models import Profesores
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

# Create your views here.

class mostrarProfesor(ListView):
    model = Profesores
    template_name = 'academico/profesor/index.html'

class registrarProfesor(CreateView):
    model = Profesores
    form_class = profesorForm
    template_name = 'academico/profesor/registrarProfesor.html'
    success_url = reverse_lazy('profesores')

class profesorUpdate(UpdateView):
    model = Profesores
    form_class = profesorForm
    template_name = 'academico/profesor/editar.html'
    success_url = reverse_lazy('profesores')

class profesorDelete(DeleteView):
    model = Profesores
    template_name = 'academico/profesor/eliminar.html'
    success_url = reverse_lazy('profesores')