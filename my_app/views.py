from django.shortcuts import render
from .models import Viajes

# Create your views here.


def viajes_views(request):
    data = Viajes.objects.all()
    context = data
    return render(request, "viajes.html", context={"viajes": context})


def index(request):
    return render(request, "index.html")
