from django.shortcuts import render, redirect
from apps.carreras.forms import carreraForm, especialidadForm, FileFormCarrera
from apps.carreras.models import Carrera, Especialidad
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import tempfile, openpyxl
from django.http import HttpResponse

# Create your views here.

"""class mostrarCE(ListView):
    model = Carrera Especialidad
    template_name = 'carreras/index.html'"""
def mostrarCarrera(request):
    if request.method == 'POST':
        form = FileFormCarrera(request.POST, request.FILES)
        if form.is_valid():
            import_file = form.cleaned_data['file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            print(import_file)
            with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as uploaded_file:
                for chunk in import_file.chunks():
                    uploaded_file.write(chunk)
            print(uploaded_file.name)
            book = openpyxl.load_workbook(uploaded_file.name)
            sheet = book.active
            for row in range(sheet.min_row, sheet.max_row+1):
                try:
                    Carrera.objects.get_or_create(
                        carrera=sheet.cell(row=row, column=1).value,
                        clave=sheet.cell(row=row, column=2).value,
                        color=sheet.cell(row=row, column=3).value)
                except:
                    print("Error al registrar Carrera")
            return redirect('carrera')
    if request.method == 'GET':
        carrera = Carrera.objects.all()
        especialidad = Especialidad.objects.all()
        form = FileFormCarrera()
        contexto = {'carreras': carrera, 'especialidades': especialidad, 'form': form}
        return render(request, 'carreras/index.html', contexto)
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
