Óscar Moreira Estévez

# FTP Windows y Linux

![portada](./img/portada.jpg)

___

# Práctica

En esta práctica veremos como se instala y configura un servidor *FTP* tanto en Linux como en Windows server 2012.

También haremos pruebas y conexiones desde un cliente en cada uno de los casos.

# Procedimiento

# 1. Windows Server 2012

## 1.1 Instalación FTP Windows Server 2012

- Lo primero que haremos sera ir a `agregar roles y características`.

- Dentro eligiremos la opción `Instalación basadad en roles y características`.

  ![1_inicio](./img/windows/1.png)

- Después eligiremos el servidor.

  ![2_inicio](./img/windows/2.png)

- Pasaremos a `Roles de servidor` y activaremos la casilla `Servidor FTP`.

  ![3_inicio](./img/windows/3.png)

- Pasaremos a las `Características` y lo dejaremos como está.

  ![4_inicio](./img/windows/4.png)

- En el siguiente paso confirmamos e instalamos.

  ![5_inicio](./img/windows/5.png)

- Luego iremos al panel de nuevo y entramos en  `Herramientas`-->`Administrador de Information Services (IIS)`

  ![6_inicio](./img/windows/6.png)

- Una vez dentro ya veremos que nos sale un panel de *FTP*.

  ![7_inicio](./img/windows/7.png)

___

## 1.2 Creacion de sitios FTP

Crearemos diferentes sitios webs con usuarios para cada uno y aparte instalaremos un programa llamado ***WinSCP*** en el cliente.

### 1.2.1 FTP de Administrador

Este sitio estara asociado a la unidad C: completa, y su usuario se llamará Administrador con permisos de lectura y escritura y sin certificado SSL.

- Primero iremos al panel y entramos en  `Herramientas`-->`Administrador de Information Services (IIS)`

  ![8 sitios ftp](./img/windows/6.png)

- Una vez dentro iremos al servidor y clicaremos botón derecho en `sitios`-->`agregar sitio ftp`

  ![9 sitio ftp](./img/windows/1/9.png)

- Ahora le pondremos nombre sl sitio ftp y eligiremos el directorio que queremos tener como contenido. En nuestro caso el disco C: completo

  ![10 sitio ftp](./img/windows/1/10.png)

- Pasamos a la configuración de enlaces y SSL.

  ![11 sitio ftp](./img/windows/1/11.png)

- Ahora en la autenticación y autorización le diremos que será `basica` y le pondremos que será el usuario llamado `Administrador` y los permisos correspondientes.

  ![13 sitio ftp](./img/windows/1/13.png)

#### Comprobación:

- **Desde localhost:**

  - Iremos a navegador o a la ruta en carpetas y pondremos : `ftp://localhost` esto nos pedirá una contraseña.

    ![14 sitio ftp](./img/windows/1/14.png)

  - Entramos y veremos que nos sale todo el contenido del disco local C:

    ![15 sitio ftp](./img/windows/1/15.png)

- **Desde cliente windows 10:**

  - Iremos a navegador o a la ruta en carpetas y pondremos : `ftp://IP_SERVIEOR` esto nos pedirá una contraseña.

    ![16 sitio ftp](./img/windows/1/16.png)

  - Entramos y veremos que nos sale todo el contenido del disco local C:

    ![17 sitio ftp](./img/windows/1/17.png)

- **Desde WinSCP en cliente:**

  - Entraremos en el programa y eligiremos protocolo *FTP* sin cifrado,la IP del servidor y el puerto 21.

    ![18 sitio ftp](./img/windows/1/18.png)  

  - Veremos que nos salen todo el contenido del disco local C:

    ![19 sitio ftp](./img/windows/1/19.png)

___

### 1.2.2 FTP de todos los usuarios

En este sitio el contenido sera `/inetpub/wwwroot` con acceso para todos los usuarios de Active Directory con permisos de escritura y lectura y con permitir SSL.

- Creamos un nuevo sitio FTP

- Ahora le daremos un nombre al sitio ftp y tambien elegiremos la ruta que tendra el contenido en este caso: `inetpub/wwwroot`

  ![1 2sitio ftp](./img/windows/2/1.png)

  ![2 2sitios ftp](./img/windows/2/2.png)

- Pasaremos a la `Confifguración de enlaces y SSL` y le pondremos en `permitir SSL` y elegimos un certificado.

  ![4 2sitio](./img/windows/2/4.png)

- Luego en el siguiente paso eligiremos  autenticación básica y autorización a todos los usuarios.

  ![5 2sitio](./img/windows/2/5.png)

#### Comprobación

- **Desde localhost:**

  - Iremos a navegador o a la ruta en carpetas y pondremos : `ftp://localhost` esto nos pedirá una contraseña.

    ![6 2sitio ftp](./img/windows/2/6.png)

  - Entramos y veremos que nos sale todo el contenido de la ruta `/inetpub/wwwroot`:

    ![7 2sitio ftp](./img/windows/2/7.png)

- **Desde cliente windows 10:**

  - Iremos a navegador o a la ruta en carpetas y pondremos : `ftp://IP_SERVIEOR` esto nos pedirá una contraseña.

    ![8 2sitio ftp](./img/windows/2/8.png)

  - Entramos y veremos que nos sale todo el contenido de la ruta `/inetpub/wwwroot`:

    ![9 2sitio ftp](./img/windows/2/9.png)

- **Desde WinSCP en cliente:**

  - Entraremos en el programa y eligiremos protocolo *FTP* con cifrado explícito,la IP del servidor y el puerto 21.

    ![10 2sitio ftp](./img/windows/2/10.png)  

  - Entramos y veremos que nos sale todo el contenido de la ruta `/inetpub/wwwroot`:

    ![13 sitio ftp](./img/windows/2/13.png)

  ___

### 1.2.3 FTP anónimo

El tercer sitio *FTP* lo asociaremos a cualquier carpeta que tengamos en el sistema que no sea importante, permitiremos acceso anónimo y solo tendrá permisos de lectura.

- Creamos un nuevo sitio FTP

- Ahora le daremos un nombre al sitio ftp y tambien elegiremos cualquier ruta siempre que en este caso el directorio no sea importante.

  ![1 3sitio ftp](./img/windows/3/1.png)


- Pasaremos a la `Confifguración de enlaces y SSL` y le pondremos en `sin SSL` y

  ![2 3sitio](./img/windows/3/2.png)

- Luego en el siguiente paso eligiremos  autenticación básica y autorización a `usuarios anónimos`.

  ![3 3sitio](./img/windows/3/3.png)

#### Comprobación

Antes de la comprobación le daremos permisos al grupo todos a la carpeta que hemos elegido para el *ftp anónimo*.

  ![4 3sitio ftp](./img/windows/3/4.png)

- **Desde localhost:**

  - Iremos a navegador o a la ruta en carpetas y pondremos : `ftp://localhost` esto no nos pedirá una contraseña ya que es para todos los usuarios anónimos.

  - Entraremos directamente en la carpeta.

    ![5 3sitio ftp](./img/windows/3/5.png)


- **Desde WinSCP en cliente:**

  - Entraremos en el programa y eligiremos protocolo *FTP* sin cifrado ,la IP del servidor y el puerto 21.

    ![6 6sitio ftp](./img/windows/3/6.png)  

  - Entramos y veremos que nos saldrá el contenido  de la carpeta.

    ![7 sitio ftp](./img/windows/3/7.png)

___
___

## 1.3 FTP con DNS

Crearemos un DNS llamado *ftp.miempresa.com* y comprobaremos que podemos acceder por el nombre que le hemos dado.

- Iremos a *IIS* y eligiremos un sitio ftp de los que hemos creado e iremos al panel derecho a `enlaces`

  ![0 dns](./img/windows/4/0.png)

- una vez dentro agregaremos un enlace y lo pondremos como `http`, `puerto 80`, y el nombre que le queremos dar `ftp.miempresa.com`.

  ![1 dns](./img/windows/4/1.png)

### Comprobación

- **Desde servidor:**

  ![2 dns](./img/windows/4/2.png)

- **Desde cliente:**

  ![3 dns](./img/windows/4/3.png)

___
___

## 1.4 FTP varios a la vez.

En un principio es posible que debas detener un sitio web para que pueda iniciarse otro. Tras comprobar el funcionamiento por separado de los sitios, encontrar una solución para que nuestro servidor ofrezca varios sitios FTP simultáneamente.

- Lo que podemos hacer es cambiarle el puerto a cada ftp y asi poder entrar en ellos sin tener que estar desconectandolos y conectandolos.

- Iremos a *IIS* y eligiremos un sitio ftp e iremos al panel derecho a `enlaces` y entramos y editamos el enlace poniendole otro puerto.

  ![1 fin](./img/windows/5/1.png)

- Como vemos ahora estan los dos conectados.

  ![6 fin](./img/windows/5/6.png)

### Comprobación

- **Ftp inetpub:**

  ![2 fin](./img/windows/5/2.png)

  ![3 fin](./img/windows/5/3.png)

- **Ftp anónimo:**

  ![4 fin](./img/windows/5/4.png)

  ![5 fin](./img/windows/5/5.png)

___
___
___

# 2. Linux Ubuntu 16.04

## 2.1 SSH

- Lo primero que haremos será instalar el servicio *SSH*: `sudo apt install openssh-server`

  ![1 linux](./img/linux/1.png)

## 2.2 Crear usuarios y permisos

- Ahora crearemos 2 usuarios que usaremos para conectarnos en remoto. `sudo adduser usuario1`

  > Le pondremos contraseña al usuario

  ![2 linux](./img/linux/2.png)

- Haremos lo mismo con otro usuario llamado *usuario2*

- Ahora iremos a `Configuración`-->`Cuentas de usuario` y a uno de los dos usuario le pondemos como administrador y al otro como estandar.

  ![3 linux](./img/linux/3.png)

## 2.3 Conexión SSH

> Desde el cliente

- Para conectarnos al servidor a uno de los usuarios creador haremos: `ssh usuario@IP_SERVIDOR`

- Ahora vemos como estamos dentro de cada uno de ellos.

  - **Usuario1:**

      ![5 linux](./img/linux/5.png)

  - **Usuario2:**

      ![4 linux](./img/linux/4.png)

## 2.4 Ejecutar aplicación gráfica con SSH

- Para ejecutar una aplicación gráfica en remoto por SSH tendremos que ejecutar el siguiente comando: `ssh -X -p 22 usuario@IP_SERVIDOR nombre_app`

    ![6 linux](./img/linux/6.png)

## 2.5 Acceso remoto por SFTP

#### Usuario1

- Para conectarnos por sftp haremos como con ssh: `sftp usuario@IP_SERVIDOR`

  ![7 linux](./img/linux/7.png)

- Ahora pasamos a descargar en remoto un fichero que esta en el servidor a nuestra máquina cliente con el comando `get`.

  ![8 linux](./img/linux/8.png)

- Vemos que se nos ha descargado en el cliente:

  ![9 linux](./img/linux/9.png)

- Ahora haremos lo contrario subir un fichero desde el cliente al Servidor con el comando `put`

  ![10 linux](./img/linux/10.png)

- Comprobamos que lo tenemos en el servidor.

  ![11 linux](./img/linux/11.png)

#### Usuario2

- Ahora haremos lo mismo pero con el usuario2

- Para conectarnos por sftp haremos como con ssh: `sftp usuario@IP_SERVIDOR`

- Ahora pasamos a descargar en remoto un fichero que esta en el servidor a nuestra máquina cliente con el comando `get` con el usuario1

- Y vemos que se nos ha descargado en el cliente.

  ![12 linux](./img/linux/12.png)

- Ahora haremos lo contrario subir un fichero desde el cliente al Servidor con el comando `put`

  ![13 linux](./img/linux/13.png)

- Comprobamos que lo tenemos en el servidor.

  ![14 linux](./img/linux/14.png)

## 2.6 SCP transferir ficheros.

- Otra forma de transferir ficheros o carpetas, etc... es con el comando `scp`

  ~~~
  scp nombre_fichero usuario@IP_SERVIDOR:/directorio      # Esto si es solo un fichero

  scp -r nombre_fichero usuario@IP_SERVIDOR:/directorio   # Esto si es una carpeta con varios contenidos dentro.
  ~~~

- Ahora pasaremos a transferir una carpeta del cliente al servidor al usuario1

  ![15 linux](./img/linux/15.png)

- Vemos que la carpeta se ha pasado al servidor.

  ![16 linux](./img/linux/16.png)

- Haremos lo mismo pero al usuario2.

  ![17 linux](./img/linux/17.png)

- Confirmamos que se ha pasado la carpeta.

  ![18 linux](./img/linux/18.png)

## 2.7 Proftpd

- Vamos a instalar *Proftpd* con el comando `sudo apt install proftpd`

  ![19.0 linux](./img/linux/19.0.png)

- En medio de la instalación nos saldrá un mensaje en el que eligiremos la configuración como `independiente`

  ![19 linux](./img/linux/19.png)

## 2.8 Editar fichero proftpd.conf

- Iremos a la ruta donde se encuentra el fichero `/etc/proftpd/proftpd.conf` y lo abriremos con editor de texto.

- Dentro del fichero buscarmemos `#DefaultRoot` que estará comentado, lo que haremos será descomentarlo. Esta línea será la que diga que directorio van a poder ver los usuarios

- En mi caso lo configure de tal manera que el usuario1 tenga permiso a todo el disco y el usuario2 solo a su *home*

  ![20 linux](./img/linux/20.png)

## 2.9 FTP por proftpd

- Nos conectaremos con el comando `ftp IP_SERVIDOR` y esto nos pedirá un usuario y una contraseña.

- Haremos la conexión con los dos usuarios. y veremos como nos señala que nos estamos conectando por `proftpd`

  ![21 linux](./img/linux/21.png)

  ![22 linux](./img/linux/22.png)

- Ahora descargaremos algo del servidor con el comando `get` y veremos el resultado.

  ![23 linux](./img/linux/23.png)
___
___

Fín de la práctica
