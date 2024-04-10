from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Moderadores(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} -------- Apellido: {self.apellido} --------- Edad: {self.edad} --------- Correo: {self.correo}"

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()

class Colaborador(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} -------- Apellido: {self.apellido} --------- Edad: {self.edad} --------- Correo: {self.correo}"
    
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()

class Automóvil(models.Model):

    def __str__(self):
        return f"Marca: {self.marca} -------- Modelo: {self.modelo} --------- Año: {self.año} --------- Categoria: {self.categoria}"

    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    año = models.IntegerField()
    categoria = models.CharField(max_length=60)
    

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)