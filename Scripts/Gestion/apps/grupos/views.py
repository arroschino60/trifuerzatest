from django.shortcuts import render
from apps.grupos.forms import grupoForm
from apps.grupos.models import Grupos
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

# Create your views here.

class mostrarGrupo(ListView):
    model = Grupos
    template_name = 'academico/grupo/index.html'

class registrarGrupo(CreateView):
    model = Grupos
    form_class = grupoForm
    template_name = 'academico/grupo/registrarGrupo.html'
    success_url = reverse_lazy('grupos')

class grupoUpdate(UpdateView):
    model = Grupos
    form_class = grupoForm
    template_name = 'academico/grupo/editar.html'
    success_url = reverse_lazy('grupos')

class grupoDelete(DeleteView):
    model = Grupos
    template_name = 'academico/grupo/eliminar.html'
    success_url = reverse_lazy('grupos')