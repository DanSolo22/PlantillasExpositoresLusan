from django.db import models
from django.contrib.auth.models import AbstractUser


class Material(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return str(self.pk) + " - " + self.tipo


class Expositor(models.Model):
    alto = models.IntegerField(default=0)
    ancho = models.IntegerField(default=0)
    ganchosF = models.IntegerField(default=0)
    ganchosC = models.IntegerField(default=0)
    '''upload_to -> carpeta donde se guardaran las imagenes'''
    imagen_expositor = models.ImageField(default="False", upload_to="imagenes_expositor")

    def __str__(self):
        return "Alto = " + str(self.alto) + ", ancho = " + str(self.ancho) + ", ganchos por fila = " + str(
            self.ganchosF) + \
               ", gancho por columna = " + str(self.ganchosC)


class Blister(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=50)
    largo = models.IntegerField(default=0)
    ancho = models.IntegerField(default=0)

    def __str__(self):
        return "Material = " + str(self.material) + ", referencia = " + str(self.referencia) + \
               ", tamaño = " + str(self.largo) + " X " + str(self.ancho)
