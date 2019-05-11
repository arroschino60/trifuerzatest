from django.shortcuts import render
# Create your views here.

def inicio(request):
    contexto = object
    return render(request,'inicio/index.html', False)