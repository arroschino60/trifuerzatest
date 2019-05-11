from django.db import models
#from apps.especialidades.models import Especialidad

# Create your models here.

class Carrera(models.Model):
    #id_carrera = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=50, unique=True)
    clave = models.CharField(max_length=8, unique=True)
    color = models.CharField(max_length=15)
    #especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)

class Especialidad(models.Model):
    #id_especialidad = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=50, unique=True)
    clave = models.CharField(max_length=8, unique=True)
    color = models.CharField(max_length=15)
    planEstudios = models.CharField(max_length=15)

