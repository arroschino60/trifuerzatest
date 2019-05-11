from django.db import models

# Create your models here.

class Atributo(models.Model):
    atributo = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return '{}'.format(self.atributo)

class Criterio(models.Model):
    criterio = models.CharField(max_length=100, unique=True)
    atributo = models.ForeignKey(Atributo, null=False, blank=True, on_delete=models.CASCADE)