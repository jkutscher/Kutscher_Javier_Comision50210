from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from CarAPP.models import *

class ModeradoresFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    correo = forms.EmailField()

class ColaboradorFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    correo = forms.EmailField()

class AutomóvilFormulario(forms.Form):

    marca = forms.CharField(max_length=60)
    modelo = forms.CharField(max_length=60)
    año = forms.IntegerField()
    categoria = forms.CharField(max_length=60)

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]