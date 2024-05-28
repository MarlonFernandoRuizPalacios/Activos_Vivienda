from django.shortcuts import render
from django.http import HttpResponse
from .models import inventtario, Activo

def home(request):
    inventarios = inventtario.objects.all()  # Cambié el nombre de la variable
    return render(request, 'index.html', {'inventarios': inventarios})

def index(request):
    activos = Activo.objects.all()
    return render(request, 'index.html', {'activos': activos})
