import re
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Alumno, Comentarios, Cursos
from .forms import AlumnoForm, UserRegisterForm, ComentariosForm

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html')

def registro(request):

    alumnos = Alumno.objects.all

    return render(request, 'miapp/registro.html', {'alumnos':alumnos})

def ingresoalumnos(request):
    form = AlumnoForm()
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = Alumno()
            alumno.nombre = form.data['nombre']
            alumno.apellido = form.data['apellido']
            alumno.edad = form.data['edad']
            alumno.email = form.data['email']
            alumno.save()
            messages.success(request, f'El alumno {alumno.nombre} {alumno.apellido} a sido Registrado Correctamente')

    return render(request, 'miapp/ingresoal.html', {'form':form})

def singup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El Usuario {username} a sido Registrado Correctamente')
    else:
        form = UserRegisterForm()

    context = {'form':form}

    return render(request, 'miapp/signup.html', context)

@login_required
def ingresado(request):
    return render(request, 'miapp/ingresado.html')

def listarcursos(request):
    
    cursos = Cursos.objects.all()

    return render(request, 'miapp/listarcursos.html', {'cursos':cursos})


def crearcomentario(request):
    form = ComentariosForm()
    if request.method == 'POST':
        form = ComentariosForm(data=request.POST)
        comentario = form.save(commit=False)
        comentario.save()
        return redirect('listarcomentarios')

    else:
        return render(request, 'miapp/crearcomentario.html', {'form':form})

def listarcomentarios(request):
    comentarios = Comentarios.objects.all()

    return render(request, 'miapp/listarcomentarios.html', {'comentarios': comentarios})

def editarcomentarios(request, id):
    comentario = Comentarios.objects.get(pk=id)
    form = ComentariosForm(instance=comentario)
    if request.method == 'POST':
        form = ComentariosForm(data=request.POST, instance=comentario)
        form.save()
        return redirect('listarcomentarios')
    else:
        return render(request, 'miapp/editarcomentario.html', {'form':form})

def borrarcomentarios(request, id):
    comentario = Comentarios.objects.get(pk=id)
    comentario.delete()
    return redirect('listarcomentarios')