from django.shortcuts import render
from django.http import HttpResponse
from CarAPP.models import *
from .forms import *
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def sobremi(request):

    return render(request, "sobremi.html")

def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "inicio.html", {"mensaje":"Usuario Creado."})
    
    else:

        form = UsuarioRegistro()

    return render(request, "registro.html", {"formulario": form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f"Bienvenido {user}"})
            
        else:

            return render(request, "inicio.html", {"mensaje": f"Los datos son incorrectos."})
        
    else:

        form = AuthenticationForm()

    return render(request, "login.html", {"formulario": form})

def logout_view(request):

    logout(request)

    return render(request, "logout.html")

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "inicio.html", {"mensaje": "Usuario Actualizado."})
        
    else:

        form = FormEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,

        })
    
    return render(request, "editarperfil.html", {"formulario":form, "usuario": usuario})

### MODERADORES ###

def crearModeradores(request):

    if request.method == "POST":

        formulario1 = ModeradoresFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            moderador = Moderadores(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], correo=info["correo"])

            moderador.save()

            return render(request, "inicio.html")
        
    else:

        formulario1 = ModeradoresFormulario()

    return render(request, "crearmoderadores.html", {"form1": formulario1})

def leerModeradores(request):

    moderador = Moderadores.objects.all()

    contexto = {"Mods": moderador}

    return render(request, "leermoderadores.html", contexto)

def eliminarModeradores(request, modNombre):

    moderador = Moderadores.objects.get(nombre=modNombre)
    moderador.delete()

    moderador = Moderadores.objects.all()

    contexto = {"Mods": moderador}

    return render(request, "leermoderadores.html", contexto)

def editarModeradores(request, modNombre):

    moderador = Moderadores.objects.get(nombre=modNombre)

    if request.method == "POST":

        formulario1 = ModeradoresFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            moderador.nombre = info["nombre"]
            moderador.apellido = info["apellido"]
            moderador.edad = info["edad"]
            moderador.correo = info["correo"]

            moderador.save()

            return render(request, "inicio.html")
        
    else:

        formulario1 = ModeradoresFormulario(initial={"nombre":moderador.nombre, "apellido":moderador.apellido, "edad":moderador.edad, "correo":moderador.correo})

    return render(request, "editarmoderadores.html", {"form1": formulario1, "nombre":modNombre})

### COLABORADORES ###
def crearColaboradores(request):

    if request.method == "POST":

        formulario1 = ColaboradorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            colaborador = Colaborador(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], correo=info["correo"])

            colaborador.save()

            return render(request, "inicio.html")
        
    else:

        formulario1 = ColaboradorFormulario()

    return render(request, "crearcolaboradores.html", {"form1": formulario1})

def leerColaboradores(request):

    colaborador = Colaborador.objects.all()

    contexto = {"Colab": colaborador}

    return render(request, "leercolaboradores.html", contexto)

def eliminarColaboradores(request, colabNombre):

    colaborador = Colaborador.objects.get(nombre=colabNombre)
    colaborador.delete()

    colaborador = Colaborador.objects.all()

    contexto = {"Colab": colaborador}

    return render(request, "leercolaboradores.html", contexto)

def editarColaboradores(request, colabNombre):

    colaborador = Colaborador.objects.get(nombre=colabNombre)

    if request.method == "POST":

        formulario1 = ColaboradorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            colaborador.nombre = info["nombre"]
            colaborador.apellido = info["apellido"]
            colaborador.edad = info["edad"]
            colaborador.correo = info["correo"]

            colaborador.save()

            return render(request, "inicio.html")
        
    else:

        formulario1 = ColaboradorFormulario(initial={"nombre":colaborador.nombre, "apellido":colaborador.apellido, "edad":colaborador.edad, "correo":colaborador.correo})

    return render(request, "editarcolaboradores.html", {"form1": formulario1, "nombre":colabNombre})

### AUTOMOVILES ###
@login_required
def crearAutomoviles(request):

    if request.method == "POST":

        formulario1 = AutomóvilFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            Automovil = Automóvil(marca=info["marca"], modelo=info["modelo"], año=info["año"], categoria=info["categoria"])

            Automovil.save()

            return render(request, "inicio.html", {"mensaje": "Automóvil creado con éxito."})
        
    else:

        formulario1 = AutomóvilFormulario()

    return render(request, "crearautomoviles.html", {"form1": formulario1})

@login_required
def leerAutomoviles(request):

    automovil = Automóvil.objects.all()

    contexto = {"Autos": automovil}

    return render(request, "leerautomoviles.html", contexto)

@login_required
def eliminarAutomoviles(request, autosNombre):

    automovil = Automóvil.objects.get(marca=autosNombre)
    automovil.delete()

    automovil = Automóvil.objects.all()

    contexto = {"Autos": automovil}

    return render(request, "leerautomoviles.html", contexto)

@login_required
def editarAutomoviles(request, autosNombre):

    automovil = Automóvil.objects.get(marca=autosNombre)

    if request.method == "POST":

        formulario1 = AutomóvilFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            automovil.marca = info["marca"]
            automovil.modelo = info["modelo"]
            automovil.año = info["año"]
            automovil.categoria = info["categoria"]

            automovil.save()

            return render(request, "inicio.html")
        
    else:

        formulario1 = AutomóvilFormulario(initial={"marca":automovil.marca, "modelo":automovil.modelo, "año":automovil.año, "categoria":automovil.categoria})

    return render(request, "editarautomoviles.html", {"form1": formulario1, "nombre":autosNombre})

@login_required
def agregarAvatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save

            return render(request, "inicio.html")
        
    else:

        form = AvatarFormulario()
    
    return render(request, "agregaravatar.html", {"formulario": form})