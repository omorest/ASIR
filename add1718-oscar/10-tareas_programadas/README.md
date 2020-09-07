Óscar Moreira Estévez

# Tareas programadas

![portada](./img/portada.png)

# 1. Windows

## 1.1 Tarea diferida

En el caso de las tareas diferidas son solo para que se ejecuten una vez en una fecha futura, pero solo una vez.

- Iremos al `Panel de control` y buscaremos **herramientas**.

  ![1](./img/1.png)

- Una vez dentro de `herramientas` buscaremos la herramienta `Programador de tareas`.

  ![2](./img/2.png)

- Dentro del *Programador de tareas* iremos al panel derecho y entraremos en `Crear una tarea básica`.

  ![3](./img/3.png)

- En mi caso ejecuto un fichero *txt*.

- Dentro de la creación de una tarea básica le pondremos el nombre y una descripción.

  ![4](./img/4.png)

- En el siguiente paso le diremos que lo ejecute solo una vez ya que es una tarea diferida.

  ![5](./img/5.png)

- Luego eligiremos una fecha y hora.

  ![6](./img/6.png)

- A continucación indicamos `Iiciar un programa`

  ![7](./img/7.png)

- Eligimos la ruta al programa o fichero.

  ![8](./img/8.png)

- Y finalizamos la creación.

  ![9](./img/9.png)

Vemos que el fichero *txt* se ha ejecutado a la hora que hemos programado.

  ![10](./img/10.png)

___

## 1.2 Tarea periódica

Una tarea periódica a diferencia de la diferida, será que se ejcuta cada intervalo de tiempo.

- Volveremos al panel del `Programador de tareas`y entramos en `Crear una tarea básica`.

- Le pondremos nombre y definición.

  ![11](./img/11.png)

- Le pondremos que se ejecute diariamente.

  ![12](./img/12.png)

- Luego le indicaremos la fecha de inicio, la hora y cada cuantos días se repetirá.

  ![13](./img/13.png)

- Después de esto activaremos la opción `Iniciar un programa`.

  ![14](./img/14.png)

- Nuestra tarea será indicarle que se apague solo el ordenador cada día a cierta hora.

- Por lo que en *programa o script* pondrmeos el comando `shutdown` y en argumentos pondremos `/s`.

  ![15](./img/15.png)

- Finalizamos la creación de la tarea.

  ![16](./img/16.png)

Veremos que cuando llegue la hora que le hemos indicado se nos apagará el pc.

  ![17](./img/17.png)

___
___

# 2. Linux - OpenSUSE

## 2.1 Tarea diferida

- Lo primero que tenemos que hacer será activar el servicio `atd` que será el que nos permita ejecutar los comandos **at**.

- Iremos a `yast`--> `Administrador de servicios`.

  ![20](./img/20.png)

- Y habilitamos y activamos el servicio `atd`.

  ![20](./img/2.png)

- Para verificar que esta funcionando haremos: `sudo systemctl status atd`

  ![21](./img/21.png)

- Si ejecutamos el comando `atq` veremos que no hay tareas progradas.

  ![23](./img/23.png)

- Ahora creamos un script que nos dará un mensaje de aviso en la pantalla.

  ![24](./img/24.png)

  ![25](./img/25.png)

- Instalamos `zenity`.

  ![26](./img/26.png)

- Ahora creamos una tarea diferida  cone el comando `at` y verificamos con `atq`  que hay una tarea programada.

  ![27](./img/27.png)

- Si hacemos `at -c 1` veremos la configuración de la primera tarea, en nuestro caso es la 4.

  ![29](./img/29.png)

- Ahora cuando llegue la hora programada veremos que nos muestra el mensaje en pantalla.

  ![28](./img/27.png)

- `atq` para ver que no hay tareas programadas.
___

## 2.2 Tarea periódica.

- Para las tareas periódicas usaremos el comando `crontab`.

- Primero ejecutaremos `crontab -l` para ver que no hay tareas.

  ![31](./img/31.png)

- Usaremos `contrab -e` para abrir el editor que por defecto es el `vim` para la configuración .

- Definimos una tarea periódica para apagar el pc a una hora en concreto cada cierto tiempo.

  ![32](./img/32.png)

- Si ahora ejecutamos `crontab -l` veremos que hay una tarea programada.

La máquina se ha apagado pero no se puede hacer captura del apagado, aunque el proceso hecho esta todo correcto ya que ha funcionado.

___
___

Fín de la práctica
