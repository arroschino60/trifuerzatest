from django.db import models

# Create your models here.

class Roles(models.Model):
    rol = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return '{}'.format(self.rol)

class Profesores(models.Model):
    nombre = models.CharField("Nombre(s) del Profesor", max_length=50)
    ap_Pat = models.CharField("Apellido Paterno", max_length=25)
    ap_Mat = models.CharField("Apellido Materno", max_length=25)
    email = models.EmailField()
    password = models.CharField("Password", max_length=30)
    rol = models.ForeignKey(Roles, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {} {}'.format(self.nombre,self.ap_Pat,self.ap_Mat)