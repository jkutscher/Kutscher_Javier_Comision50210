from django.urls import path
from CarAPP.views import *


urlpatterns = [

#PRINCIPALES
    
    path('', inicio, name="Inicio"),
    path('sobremi/', sobremi, name="Sobremi"),
    path('login/', login_request, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', logout_view, name="Logout"),
    path('editarperfil/', editarUsuario, name="Editar_Usuario"),
    path('agregaravatar/', agregarAvatar, name="Avatar"),


#CRUD de Moderadores
    path('crearmoderadores/', crearModeradores, name="Crear_Moderadores"),
    path('leermoderadores/', leerModeradores, name="Leer_Moderadores"),
    path('eliminarmoderadores/<modNombre>/', eliminarModeradores, name="Eliminar_Moderadores"),
    path('editarmoderadores/<modNombre>', editarModeradores, name="Editar_Moderadores"),

#CRUD de Colaboradores
    path('crearcolaboradores/', crearColaboradores, name="Crear_Colaboradores"),
    path('leercolaboradores/', leerColaboradores, name="Leer_Colaboradores"),
    path('eliminarcolaboradores/<colabNombre>/', eliminarColaboradores, name="Eliminar_Colaboradores"),
    path('editarcolaboradores/<colabNombre>', editarColaboradores, name="Editar_Colaboradores"),

#CRUD de Automoviles usando clases
    path('crearautomoviles/', crearAutomoviles, name="Crear_Automoviles"),
    path('leerautomoviles/', leerAutomoviles, name="Leer_Automoviles"),
    path('eliminarautomoviles/<autobNombre>/', eliminarAutomoviles, name="Eliminar_Automoviles"),
    path('editarautomoviles/<autobNombre>', editarAutomoviles, name="Editar_Automoviles"),

]