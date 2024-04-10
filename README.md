# EntregaFinal-Javier Kutscher

### Instalacion requerida
Para ver este proyecto es necesario tener instalado Django y en un principio ejecutar las siguientes lineas de codigo para evitar posibles errores.

1- Para que se cree la base de datos en donde haremos la interaccion, posicionandose en terminal en la carpeta que contiene el archivo *manage.py* haremos:

*windows*
```bash
  python manage.py makemigrations 
```
```bash
  python manage.py migrate 
``` 
*MacOS*
```bash
  python3 manage.py makemigrations 
```
```bash
  python3 manage.py migrate 
``` 

2- Para ejecutar el servidor que nos permitirá ver la pagina en un navegador habra que ejecutar el siguiente codigo:

*windows*
```bash
  python manage.py runserver 
```
*MacOS*
```bash
  python3 manage.py runserver
```

Para acceder a la pagina en el navegador se debe escribir la siguiente url:
```bash
  localhost:8000/ 
```
Esto mostrara disponible dos Apps, la correspondiente a la seccion de admin y a la App de la pagina en desarrollo.

4- Se recomienda hacer una base de datos nueva y la creacion de un superuser. Para ello en terminal habra que escribir lo siguiente, y seguir las instrucciones:
*windows*
```bash
  python manage.py createsuperuser 
```
*MacOS*
```bash
  python3 manage.py createsuperuser
```

Si no se quiere crear un nuevo SuperUser el creado es:

Username: usuarioadmin
Password: python123

### Admin Page
Se puede acceder a la pagina de admin (previa la creacion del superuser) mediante la url:

```bash
  localhost:8000/admin
```

Se puede acceder a la pagina de admin mediante la url:
```bash
  localhost:8000/CarAPP/
```
La pagina en desarrollo cuenta con botones para poder navegar y realizar las acciones correspondientes para el testeo.
