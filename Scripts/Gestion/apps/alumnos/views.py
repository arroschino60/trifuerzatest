from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from apps.alumnos.forms import alumnoForm, FileForm
from apps.alumnos.models import Alumnos
from apps.carreras.models import Carrera
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
import tempfile, openpyxl

# Create your views here.

def mostrarA(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
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
                    carrera = Carrera.objects.get(carrera=sheet.cell(row=row, column=8).value)
                    Alumnos.objects.get_or_create(
                        nControl=sheet.cell(row=row, column=1).value,
                        nombre=sheet.cell(row=row, column=2).value,
                        ap_Pat=sheet.cell(row=row, column=3).value,
                        ap_Mat=sheet.cell(row=row, column=4).value,
                        email=sheet.cell(row=row, column=5).value,
                        password=sheet.cell(row=row, column=6).value,
                        fechaIngreso=sheet.cell(row=row, column=7).value,
                        carrera=carrera)
                except:
                    print   ("Carrera Inexistente")
            return redirect('alumnos')
    if request.method == 'GET':
        alumno = Alumnos.objects.all()
        paginator = Paginator(alumno, 30)
        page = request.GET.get('page')
        alumnos = paginator.get_page(page)
        form = FileForm()
        contexto = {'alumnos': alumnos, 'form': form}
        return render(request, 'academico/alumno/index.html', contexto)
"""def registrarEspecialidad(request):
    if request.method == 'POST':
        form = alumnoForm(request.POST)
        if form.is_valid():
            form.save()
        return mostrarCE(request)
    else:
        form = especialidadForm()
    return render(request, 'carreras/especialidad.html',{'form':form})"""

class mostrarAlumno(ListView):
    model = Alumnos
    template_name = 'academico/alumno/index.html'

class registrarAlumno(CreateView):
    model = Alumnos
    form_class = alumnoForm
    template_name = 'academico/alumno/registrarAlumno.html'
    success_url = reverse_lazy('alumnos')

class alumnoUpdate(UpdateView):
    model = Alumnos
    form_class = alumnoForm
    template_name = 'academico/alumno/editar.html'
    success_url = reverse_lazy('alumnos')

class alumnoDelete(DeleteView):
    model = Alumnos
    template_name = 'academico/alumno/eliminar.html'
    success_url = reverse_lazy('alumnos')