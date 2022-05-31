from django.contrib import admin
from .models import Viajes

# Register your models here.


class Display(admin.ModelAdmin):
    list_display = ("nombre", "destino", "precio", "fecha_de_partida")


admin.site.register(Viajes, Display)
