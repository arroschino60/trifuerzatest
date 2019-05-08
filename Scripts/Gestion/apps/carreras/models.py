from django.db import models
#from apps.especialidades.models import Especialidad

# Create your models here.

class Carrera(models.Model):
    #id_carrera = models.AutoField(primary_key=True)
    carrera = models.CharField("Nombre de Carrera", max_length=50, unique=True)
    clave = models.CharField("Clave de Carrera", max_length=8, unique=True)
    color = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return '{}'.format(self.carrera)
    #especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)

class Especialidad(models.Model):
    #id_especialidad = models.AutoField(primary_key=True)
    especialidad = models.CharField("Nombre de la Especialidad", max_length=50, unique=True)
    clave = models.CharField("Calve de la Especialidad", max_length=8, unique=True)
    color = models.CharField(max_length=15)
    planEstudios = models.CharField("Plan de Estudios", max_length=15)
    def __str__(self):
        return '{}'.format(self.especialidad)

