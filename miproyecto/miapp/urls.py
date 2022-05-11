from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('ingresoalumnos', views.ingresoalumnos, name='ingresoal'),
    path('signup/', views.singup, name='signup'),
    path('ingresado/',views.ingresado,name='ingresado'),
    path('listarcursos/',views.listarcursos ,name='listarcursos'),
    path('crearcomentario/',views.crearcomentario, name='crearcomentarios'),
    path('listarcomentario/',views.listarcomentarios, name='listarcomentarios'),
    path('editarcomentario/<int:id>',views.editarcomentarios, name='editarcomentarios'),
    path('eliminarcomentario/<int:id>',views.borrarcomentarios , name='eliminarcomentarios'),
]