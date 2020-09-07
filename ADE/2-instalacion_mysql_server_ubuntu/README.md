Óscar Moreira 2ºASIR

# Instalación MySQL server y phpMyAdmin

![portada](./img/portada.png)

___

 Esta práctica consiste en instalar en nuestra máquina Ubuntu 16.04 el *MySQL*, *Workbench* y *phpMyAdmin* .

___

Entraga de la práctica:

- Crear informe explicativo.
- Detallar los pasos realizados incluyendo imágenes.

___

# Máquina virtual

En este caso he realizado la práctica con una máquina con el sistema operativo `Ubuntu 16.04`.

___
___

# 1. MySQL server y cliente

- Lo primero que haremos será instalar `MySQL server` y esto se hara con el siguiente comando:

  ~~~
  sudo apt-get install mysql-server
  ~~~

  ![1.1](./img/1.1.png)

  - En medio de la instalación nos pedirá que pongamos una contraseña para el root de ***MySQL*** .

    ![1.2](./img/1.2.png)

  - Y la volveremos a poner de nuevo.

    ![1.3](./img/1.3.png)

- Veremos la versión que hemos instalado poniendo el siguiente comando:

  ~~~
  mysql-server --version
  ~~~

  ![1.4](./img/1.4.png)

  Con esto veremos que tenemos instalada la última versión `5.7.19`.

- Para verificar que el servicio esta funcionando correctamente podemos usar dos comandos:

  ~~~
  - sudo service mysql status
  - sudo systemctl status mysql
  ~~~

  ![1.5](./img/1.5.png)

  Veremos que pondrá `active (running)` significa que esta funcionando correctamente en este momento.

___

- Una vez instalado `mysql-server` pasaremos a instalar `MySQL-client`.

  ~~~
  sudo apt-get install mysql-client
  ~~~

  ![1.6](./img/1.6.png)

- Después de esto reiniciaremos el servicio.

  ![1.7](./img/1.7.png)

- También para ver si el `demonio` de ***MySQL*** esta activo podremos usar el comando:

  ~~~
  ps aux | grep mysql
  ~~~

  ![1.8](./img/1.8.png)

### Comprobación

Para comprobar que mysql funciona correctamente entraremos con el comando:

~~~
mysql -u root -p
~~~

  ![1.9](./img/1.9.png)

Con esto entraremo a la base de datos ***MySQL***.

___


# 2. MySQL secure instalation.

Cuando ejecutemos este comando nos empezará hacer preguntas para aumentar la seguridad de ***MySQL*** como por ejemplo la dificultad de la contraseña root, accesos remotos, usuarios creados automaticamente, etc...

Dejaré las imágenes de la configuración usada.

  ![1.10](./img/1.10.png)

  ![1.11](./img/1.11.png)

  ![1.12](./img/1.12.png)

___

# 3. Workbench

Ahora pasaremos a instalar ***MySQL Workbench***

- El comando para instalarlo sera el siguiente:

  ~~~
  sudo apt-get install mysql-workbench
  ~~~
  ![1.13](./img/1.13.png)

- Una vez acabada la instalación veremos que tendremos el programa y lo podremos usar.

  ![workbench](./img/workbench.png)

___

# 4. phpMyAdmin

Para instalar el ***phpMyAdmin*** usaremos este comando:

~~~
sudo apt-get install phpmyadmin
~~~

Cuando se este instalando nos hará unas preguntas:

- La primera será elegir el servidor web con el que vamos a trabajar en nuestro caso `apache`

  ![1.15](./img/1.15.png)

- El siguiente paso le daremos a que sí

  ![1.16](./img/1.16.png)


- Luego la contraseña para el root de ***phpMyAdmin***

  ![1.17](./img/1.17.png)

- Volveremos a ponerla.

  ![1.18](./img/1.18.png)

Ya terminado estos pasos se habrá acabado la instalación de ***phpmyadmin***

Si entramos ahora en la dirección **localhost/phpmyadmin** nos saldrá para poner usuario y contraseña.

Una vez puesta entraremos y veremos la configuración, podremos entrar tambien a ver los usuarios, etc..

  ![1.19](./img/1.19.png)

___
___

# 5. Indicaciones

1. Directorio de instalación base

 - Directorio: `/usr/bin`

    ![1.25](./img/1.25.png)

2. Directorio del servicio o proceso demonio

  - Directorio: `/etc/init.d`

    ![demonios](./img/demonios.png)

3. Directorio de datos

  - Directorio: `/var/lib/mysql/`

    ![1.20](./img/1.20.png)

4. Fichero de configuración del servidor y su ubicación

  - Directorio: `/etc/mysql/my.cnf`

    ![1.1](./img/1.23.png)

5. ¿Quién es el usuario propietario de la instalación ?

  - El usuario es el propio ***mysql***

      ![1.24](./img/1.24.png)

6. Aplicar el lenguaje de los mensajes de error  a español, modificando la configuración (indicar el directorio donde se aloja el fichero en español)

    - Iremos a la ruta `/usr/share/mysql/` en la que veremos que están todos los idiomas.

      ![1.21](./img/1.21.png)

    - Veremos que esta el español

      ![1.21.1](./img/1.21.1.png)

    - Después de verificar esto iremos al `workbench` y en `option file` e iremos hasta ***lc-messages-dir*** y pondremos la ruta hasta el idioma español.

      ![1.22](./img/1.22.png)

___
___

Fín de la práctica
