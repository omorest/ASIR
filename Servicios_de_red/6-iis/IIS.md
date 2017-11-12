Óscar Moreira

# Instalación y configuración IIS Windows

![portada](./img/portada.png)

___
___

# Prácticas

Este informe consistirá en 3 prácticas de de instalación y configuración de *IIS* en *Windows 12 Server*.

  **1.** Esta práctica consistirá en instalar IIS en Windows 12 Server, crear un host principal con un alias *www*, y un *index.html*

  **2.** En esta práctica deberemos crear dos nuevos sitios web, un subdominio y otro dominio asociado al principal (una nueva zona), estos dominios tendrán sus propias carpetas con sus *index.html* y lo que querramos en cada uno.

  **3.** En esta última práctica creamos directorios virtuales para uno de los dominios que hemos creado anteriormente, en el que habrá que crear mínimo 3 subcarpetas con un *index.html* cada una.

___

# Práctica 1

En la práctica 1 lo primero que haremos será instalar el rol de IIS.

- Iremos a `agregar roles y características` y una vez dentro en **selección de instalación** eligiremos `instalación basada en características o roles`.

  ![1.1](./img/1/1.1.png)

- Seguido eligiremos el servidor en el que vamos a instalar el rol y las características.

  ![1.2](./img/1/1.2.png)

- Después de haber elegido el servidor pasaremos a activar el rol de `servidor web (IIS)`, nos saldrá una ventana en la que clicaremos en `agregar características`.
