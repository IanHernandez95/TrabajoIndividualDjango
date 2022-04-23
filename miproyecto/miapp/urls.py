from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('ingresoalumnos', views.ingresoalumnos, name='ingresoal'),
    path('signup/', views.singup, name='signup'),
    path('ingresado/',views.ingresado,name='ingresado')
]