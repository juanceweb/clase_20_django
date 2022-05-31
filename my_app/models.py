from django.db import models

# Create your models here.


class Viajes(models.Model):
    nombre = models.CharField(max_length=40)
    destino = models.CharField(max_length=40)
    precio = models.IntegerField()
    fecha_de_partida = models.DateField()

    class Meta:
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"

    def __str__(self):
        return self.nombre
