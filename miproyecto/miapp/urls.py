from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('cursorevit', views.CursoRevit.as_view(), name='cursorevit'),
    path('cursoautocad', views.CursoAutocad.as_view(), name='cursoautocad'),
    path('listaralumnos', views.ListarAlumnos.as_view(), name='listaralumnos'),
    path('registraralumnos', views.RegistrarAlumnos.as_view(), name='registrar'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('listarcursos/',views.Listarcursos.as_view() ,name='listarcursos'),
    path('crearcomentario/',views.CrearComentario.as_view(), name='crearcomentarios'),
    path('listarcomentario/',views.ListarComentarios.as_view(), name='listarcomentarios'),
    path('editarcomentario/<int:pk>',views.EditarComentarios.as_view(), name='editarcomentarios'),
    path('eliminarcomentario/<int:pk>',views.EliminarComentarios.as_view() , name='eliminarcomentarios'),
]