from django import forms
from django.forms import ModelForm
from .models import Pelicula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class peliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'duracion', 'fecha', 'Genero', 'imagen']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']