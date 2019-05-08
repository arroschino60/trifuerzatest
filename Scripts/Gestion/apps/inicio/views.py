from django.shortcuts import render
from apps.carreras.models import Carrera
# Create your views here.

def inicio(request):
    carrera = Carrera.objects.all()
    contexto = {'carreras': carrera}
    #registrarCarrera(request)
    #form = carreraForm()
    return render(request, 'inicio/index.html', contexto)