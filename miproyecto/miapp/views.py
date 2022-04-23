from multiprocessing import context
from django.shortcuts import render

from .models import Alumno

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html')

def registro(request):

    alumnos = Alumno.objects.all

    return render(request, 'miapp/registro.html', {'alumnos':alumnos})

def pagina2(request):
    return render(request, 'miapp/pagina2.html')

def pagina3(request):
    return render(request, 'miapp/pagina3.html')