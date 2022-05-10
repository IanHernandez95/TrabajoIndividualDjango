from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Alumno, Comentarios

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno 
        fields = ("nombre", "apellido", "edad", "email",)



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'email', 'comentario']
