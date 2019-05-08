from django.db import models
from apps.profesores.models import Profesores

# Create your models here.
class Grupos(models.Model):
    #grupo = models.CharField(max_length=30)
    clave = models.CharField("Calve del Grupo", max_length=15)
    cantAlumnos = models.PositiveIntegerField()
    profesor = models.ForeignKey(Profesores, null=True, blank=True, on_delete=models.CASCADE)