Agenda Fenix
================

Este proyecto es una agenda que hice en Python-Django que guarda todo en una base de datos SQLite.

Funciones :

- Registro de usuario
- Ingreso de usuario
- Agregar, editar, borrar y visualizar : categorias, notas, proyectos y actividades
- Se permite insertar etiquetas html en los contenidos de las notas, proyectos y actividades
- Alarma con sonido
- Importar y exportar datos
- Muestra gráfico estadístico de cantidad de notas por categoria
- Cambiar usuario y clave de la cuenta
- Se incorporo en la version 1.1 la opcion de usar dos skins diferentes para la agenda

Cuando se importan datos se necesita seguir los siguientes pasos ...

Crear las carpetas "Actividades", "Notas" y "Proyectos".

En actividades se necesita crear un archivo de texto por cada actividad de la siguiente forma :

```
[+] Fecha : 2017-12-05
[+] Hora : 22:05:00
[+] Terminado : 0
```

Contenido de actividad

En las notas se debe crear una carpeta por cada categoria que quieran usar y por cada nota crear un archivo de texto con el título y contenido que quieran,

En los proyectos se debe crear un archivo de texto por cada proyecto de la siguiente forma :

```
[+] Fecha inicio : 2015-08-06
[+] Fecha terminado : 2018-09-10
[+] Terminado : 1
```

Contenido de proyecto

Algo a tener en cuenta es el título del archivo de texto siempre sera el título de cualquiera de las tres publicaciones.

También incluye un instalador del proyecto y launcher que evita usar manage.py para iniciar el proyecto además de hacer una copia de respaldo de la base de datos sqlite.

La versión de django que use es : 1.11.1

Imágenes :

![screenshot](https://camo.githubusercontent.com/b0d065fa505904624ad688414fb53ab2f0cd7b4c/68747470733a2f2f342e62702e626c6f6773706f742e636f6d2f2d6d7871375155426a6372552f576f696b525853627374492f41414141414141414146772f5f58784758373259544c456f48495443724d663972746f556f4d7353725a2d5a51434577594268674c2f733634302f6167656e646166656e69783130312e6a7067)

![screenshot](https://camo.githubusercontent.com/2a27602128eb873a73c39ae856b6aff6e06a246e/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d424f5866737469736933492f576f696b5248686e444f492f41414141414141414146732f594a57563447664467326b6f76764f624f58484f786a3248675a49536a514a6d77434577594268674c2f733634302f6167656e646166656e69783130322e6a7067)

![screenshot](https://camo.githubusercontent.com/8c7bce1682d36ce56cc9954539f5f75c0d91b83e/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d4c32694d753630737068672f576f696b526176786637492f41414141414141414146302f36343452374a35504f6a5957665032614836474f463236712d614e666143586c77434577594268674c2f733634302f6167656e646166656e69783130332e6a7067)

Despues de la actualizacion 1.1, la agenda se ve asi :

![screenshot](https://1.bp.blogspot.com/-3iBtQO5TIe4/XVmt16uHAmI/AAAAAAAAAlQ/76d5dDE7QZ43LwaPCmbmINTn0UnPie15gCLcBGAs/s1600/17-8-2019%2B10.8.10%2B1.jpg)

![screenshot](https://1.bp.blogspot.com/-1dlJb5Bm6Mk/XVmt2Lj9FvI/AAAAAAAAAlU/OmFm4jmB6HwTSyp4qSLamAj3Et2WjhZqgCLcBGAs/s1600/17-8-2019%2B10.8.13%2B3.jpg)
