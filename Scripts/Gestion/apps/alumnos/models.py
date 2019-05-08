from django.db import models
from apps.carreras.models import Carrera, Especialidad

# Create your models here.
class Alumnos(models.Model):
    nControl = models.CharField("Numero de Control", max_length=8, unique=True)
    nombre = models.CharField("Nombre(s) del Alumno", max_length=50)
    ap_Pat = models.CharField("Apellido Paterno", max_length=25)
    ap_Mat = models.CharField("Apellido Materno", max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField("Password", max_length=30)
    fechaIngreso = models.DateField()
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.PROTECT)
    especialidad = models.ForeignKey(Especialidad, models.SET_NULL, null=True, blank=True)