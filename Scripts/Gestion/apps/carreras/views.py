from django.shortcuts import render
from apps.carreras.forms import carreraForm, especialidadForm
from apps.carreras.models import Carrera, Especialidad
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json
from django.http import HttpResponse

# Create your views here.

"""class mostrarCE(ListView):
    model = Carrera Especialidad
    template_name = 'carreras/index.html'"""

def mostrarCE(request):
    carrera = Carrera.objects.all()
    especialidad = Especialidad.objects.all()
    contexto = {'carreras': carrera, 'especialidades': especialidad}
    #registrarCarrera(request)
    form = carreraForm()
    return render(request, 'carreras/index.html', contexto)

class registrarCarrera(CreateView):
    model = Carrera
    form_class = carreraForm
    template_name = 'carreras/registrarCarrera.html'
    success_url = reverse_lazy('carrera')

class carreraUpdate(UpdateView):
    model = Carrera
    form_class = carreraForm
    template_name = 'carreras/editarCarrera.html'
    success_url = reverse_lazy('carrera')

class carreraDelete(DeleteView):
    model = Carrera
    template_name = 'carreras/eliminarCarrera.html'
    success_url = reverse_lazy('carrera')

class registrarEspecialidad(CreateView):
    model = Especialidad
    form_class = especialidadForm
    template_name = 'carreras/registrarEspecialidad.html'
    success_url = reverse_lazy('carrera')

class especialidadUpdate(UpdateView):
    model = Especialidad
    form_class = especialidadForm
    template_name = 'carreras/editarEspecialidad.html'
    success_url = reverse_lazy('carrera')

class especialidadDelete(DeleteView):
    model = Especialidad
    template_name = 'carreras/eliminarEspecialidad.html'
    success_url = reverse_lazy('carrera')

"""def registrarCarrera(request):
    carrera = Carrera.objects.all()
    especialidad = Especialidad.objects.all()
    contexto = {'carreras': carrera, 'especialidades': especialidad}
    form = carreraForm()
    if request.method == 'POST':
        form = carreraForm(request.POST)
        if form.is_valid():
            form.save()
        return mostrarCE(request)
    else:
        form = carreraForm()
    return render(request, 'carreras/index.html', {'form': form, 'contexto':contexto})"""

    #reverse_lazy('carreras:carrera')

"""def registrarEspecialidad(request):
    if request.method == 'POST':
        form = especialidadForm(request.POST)
        if form.is_valid():
            form.save()
        return mostrarCE(request)
    else:
        form = especialidadForm()
    return render(request, 'carreras/especialidad.html',{'form':form})"""

#def eliminarCarrera(request, carrera):
#    carrera = Carrera.objects.get(pg_Carrera=carrera)
#    if request.method == 'POST'
#        form =
