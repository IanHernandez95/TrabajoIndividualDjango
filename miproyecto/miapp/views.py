from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .mixins import StaffUsuarioMixins
from .models import Alumno, Comentarios, Cursos
from .forms import AlumnoForm, UserRegisterForm, ComentariosForm

# Create your views here.+
class Index(TemplateView):
    template_name = 'miapp/index.html'


class CursoRevit(TemplateView):
    template_name = 'miapp/cursorevit.html'

class CursoAutocad(TemplateView):
    template_name = 'miapp/cursoautocad.html'

class ListarAlumnos(ListView):
    model = Alumno
    paginate_by = 10
    template_name = 'miapp/listadoalumnos.html'

class RegistrarAlumnos(LoginRequiredMixin, StaffUsuarioMixins, CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'miapp/registraralumnos.html'
    success_url = reverse_lazy('listaralumnos')

class Signup(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'miapp/signup.html'
    success_url = reverse_lazy('index')

class Listarcursos(ListView):
    model = Cursos
    template_name = 'miapp/listarcursos.html'

class CrearComentario(CreateView):
    model = Comentarios
    form_class = ComentariosForm
    template_name = 'miapp/crearcomentario.html'
    success_url = reverse_lazy('listarcomentarios')

class ListarComentarios(ListView):
    model = Comentarios
    template_name = 'miapp/listarcomentarios.html'

class EditarComentarios(UpdateView):
    model = Comentarios
    form_class = ComentariosForm
    template_name = 'miapp/crearcomentario.html'
    success_url = reverse_lazy('listarcomentarios')

class EliminarComentarios(DeleteView):
    model = Comentarios
    success_url = reverse_lazy('listarcomentarios')
