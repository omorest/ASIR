Óscar Moreira 2ºASIR

# Instalación MySQL, Workbench y pfpMyAdmind

![portada](./img/portada.png)

___

 Esta práctica consiste en instalar en nuestra máquina Windows el *MySQL*, *Workbench* y *phpMyAdmin* con el XAMPP.

 Haremos también la configuración para conexiones remotas del *Workbench*.

___

Entraga de la práctica:

- Crear informe explicativo.
- Detallar los pasos realizados incluyendo imágenes.

___

# 1. Máquina virtual

En este caso he realizado la práctica con una máquina con el sistema operativo `Windows 10`.

Tener en cuenta desactivar los *firewall*

___
___

# 2. MySQL y Workbench (MySQL community)

Usaremos una versión llamada *MySQL community* que nos traera tanto el MySQL como el Workbench cuando se elija la opción *Developer* cuando estemos instalando.


## 2.1 Instalación

Lo primero que debemos hacer antes de instalar el *Mysql* junto a *Workbench* sera instalar el ***visual c++*** así tendremos los requisitos cumplidos antes de instalar el resto.

### 2.1.1 Visual c++

1. Entrar en [visual c++](https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package)

2. Descargar el instalador en nuestro caso el español.

3. Ejecutarlo

    ![visual c++](./img/0-visual.png)

4. Instalamos y terminado.


### 2.1.2 MySQL community

Instalaremos el *MySQL community* ya que este nos instalará el MySQL junto al Workbench cuando elijamos la opción *Developer*.

Para descargarlo iremos al [enlace](https://dev.mysql.com/downloads/windows/installer/5.7.html) de *MySQL community* y descargaremos la version de 64 bits en nuestro caso.

![1](./img/1.png)


### Instalación:

Una vez descargado el instalador procederemos a instalarlo.

En este proceso nos puede pedir una contraseña *root*  asi que le pondremos la contraseña que nosotros queramos.

- Lo primero será ejecutar el instalador y nos aparecerá una pantalla así y le daremos a `Next`

  ![2](./img/2-instalacion.png)

- Luego eligiremos la opción `Developer Default` que nos instalará los productos de *MySQL* en nuestro caso para tener el *Workbench* también.

  ![2.1](./img/2.1.png)

- Pasaremos a la instalación y nos saldrá una lista de todos los productos que se instalarán, le daremos abajo a `execute`.

  ![2.2](./img/2.2.png)

- Veremos que se ponen todos en verde lo que quiere decir que todas las intalaciones se han hecho correctamente.

  ![2.3](./img/2.3.png)

- Al darle a 'Next' veremos que iremos a otro modo de instlación en el que eligiremos la primera opción `Standalone MySQL Server / Classic MySQL Replication` .

  ![2.4](./img/2.4.png)

- Pasaremos a una configuración de la opción elegida anteriormente que deberemos tener de esta manera:

  ![2.5](./img/2.5.png)

- Seguiremos hasta llegar a `Windows Service`  en el que tendremos que tener el nombre del servidor por defecto y activas las opciones que vemos.

  ![2.6](./img/2.6.png)

- Daremos siguiente y estaremos en `Plugins and Extensions` y lo dejaremos sin nada activado.

  ![2.8](./img/2.7.png)

- Finalmente daremos todo siguiente hasta terminar.

___


### Servicio MySQL

Instalado todo veremos que el servicio estará activo.

Una de las formas es ir a los servicios y ahi lo veremos.

  ![3](./img/3.png)

  ___

### Workbench

Una vez instalado el *MySQL community* lo abriremos para comprobar que esta todo correcto.


___

### Ubicación archivos

Cuando hemos instalado todo se nos creara carpetas con los archivos de configuración y directorios.

  ![3.4](./img/3.4.png)

  ![3.5](./img/3.5.png)

  ![3.6](./img/3.6.png)


  ___

## 2.2 Configuración acceso remoto

En esta parte lo que haremos sera confirar el workbench para que con usuarios podamos acceder desde otro ordenador de forma remota.

Pasos a seguir :

- Abrir *Workbench* y dentro de el ir al panel izquierdo y entrar en `Options file` y `Networking` dentro de él y activaremos abajo la casilla `bind-address` y aplicaremos el cambio.

  ![4](./img/4.png)

- Luego de esto saldra una pantallita como esta que sera para confirmar el cambio.

  ![4.1](./img/4.1.png)

- Después de esto volvemos a ir al panel de la izquierda e ir al apartado 'Users and privileges'.

  ![4.3](./img/4.3.png)

- Aquí le daremos a `Add account` para añadir un nuevo usuario con su contraseña.

  ![4.4](./img/4.4.png)

  ![4.5](./img/4.5.png)

-  En mi caso cree un usuario llamado *oscar*.

    ![4.4](./img/4.4.png)

Con esto estará todo listo para poder entrar desde otro PC de forma remota al nuestro en el que abra que poner la IP del ordenador al que nos queremos conectar el nombre del usuario y la contraseña.

___
___

# 3. XAMPP

El *XAMPP* lo utilizaremos para tener el servidor *apache* y aparte el *phpMyAdmin*.

Para instalar el *XAMPP* iremos al [enlace oficial](https://www.apachefriends.org/es/download.html) de *XAMPP* y aqui dentro eligeremos la versión que nosotros queramos pero en nuestro caso usamos la última (7.1.9 / PHP 7.1.9).

  ![5](./img/5.png)

Una vez descargado el instalador procederemos a la instalacion.

### Instalación

- Ejecutaremos el instalador y seguiremos dejando las opcionespor defecto hasta llegar a un apartado llamado `Select components`,  en este solo habrá que marcar las opciones `apache, php y phpMyAdmin `.

  ![5.1](./img/5.1.png)

- seguiremos con la instalación por defecto y listo, con esto tendremos instalado el *XAMPP* con los componentes que necesitamos.

___

### Configuración phpMyAdmin


Ahora lo que debemos hacer es configurar el *phpMyAdmin* para que tenga relación con el servidor *MySQL*.

Pasos a seguir:

- Lo primero que haremos será ir a la ruta `disco local C:/xampp/phpMyAdmin`, aqui dentro hay un fichero llamado `config.inc.php` .

  ![php1](./img/PHP1.png)

- Lo abriremos en nuestro caso con la aplicación *wordpad*.

- Una vez dentro de él viendo su información, iremos a un apartadollamado *authentication* en el que hay que poner la contraseña de root que pusimos cuando instalamos el *MySQL*

  ![php2](./img/PHP2.png)

- Cuando ya este puesto esto lo guardaremos y saldremos, abriremos el navegador y pondremos `localhost/phpmyadmin`, si entra en la página veremos que nos entra pero saldran errores, esto es porque aún no hemos terminado la configuración pero ya esta asociado al *MySQL* nuestro.

  ![php3](./img/php3.png)

- Ahora iremos a la ruta `disco local C:/xampp/phpMyAdmin/sql` y nos encontraremos un archivo llamado `create_tables.sql` que abriremos.

  ![php5](./img/php5.png)

- Copiaremos todo y lo pegaremos en una ventana del *Workbench* . También dejaré el código por aqui para poder copiarlo también.

~~~
Código a copiar:

~~~

  ![php6](./img/php6.png)

- Actualizamos el apartado del panel izquierdo llamado `SCHEMAS` y nos saldra la base de datos.

  ![php7](./img/php7.png)

- Abriremos otra ventana sql en workbench y pondremos el siguiente código.

  ~~~
  CREATE USER 'pma'@'localhost' IDENTIFIED BY 'pmapass';
  GRANT ALL PRIVILEGES ON `phpmyadmin`.* TO 'pma'@'localhost' WITH GRANT OPTION;
  FLUSH PRIVILEGES;
  ~~~

  ![php9](./img/php9.png)

- Después de hacer esto iremos de nuevo al archivo `config.inc.php` y dentro iremos a un apartado llamado `User for advanced features` en el que tendremos que poner la contraseña que pusimos en el apartado anterior.

  ![php10](./img/php10.png)

Con esto la práctica estará finalizada y veremos que si volvemos al navegador  y ponemos `localhost/phpmyadmin` ahora no nos saldrá ningun error y eso quiere decir que estara todo correcto.

  ![php11](./img/php11.png)

___

Fin de la práctica
