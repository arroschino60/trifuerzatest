from django.db import models

from apps.especialidades.models import Especialidad

# Create your models here.

class Materia(models.Model):
    materia = models.CharField(max_length=50, unique=True)
    clave = models.CharField(max_length=8, unique=True)
    credito = models.PositiveIntegerField(default=3)
    especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)