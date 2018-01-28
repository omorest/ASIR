Óscar Moreira Estévez

## Índice

- [SMTP Windows Server 2012](#smtp)

- [Hmail Windows Server 2012](#hmail)

___

<a name="smtp"></a>
# SMTP - Windows Server 2012

![portada](./img/portada.jpg)

# Instalación SMTP

- Iremos al panel del servidor y entraremos en `agregar roles y características`.

  ![1](./img/1.png)

- En el tipo de instalación eligiremos: `Instalación basada características o en roles`

  ![2](./img/2.0.png)

- Seleccionamos el servidor de destino.

  ![2.1](./img/2.1.png)

- Ahora en la selección de roles no elegimos ninguno.

  ![2.2](./img/2.2.png)

- Después de esto en la selección de características marcamos: `Servidor SMTP`

  ![2.3](./img/2.3.png)

- Y por último confirmamos la instalación.

  ![2.4](./img/2.4.png)

___

# 2. Configuración del servicio SMTP

- Para entrar en la configuración del servidor SMTP iremos al panel del servidor -->`Herramientas`-->`Administrador de Internet Information Services (IIS) 6.0`.

  ![3.0](./img/3.0.png)

- Entramos y vamos a las propiedades del servicio SMTP.

  ![3.2](./img/3.2.png)

- Ahora pondremos la IP del servidor , limitamos el numero de conexiones, y habilitamos el registro W3C.

  ![3.3](./img/3.3.png)

- Vamos a las propiedades del registro y lo dejaremos de esta manera.

  ![3.3.1](./img/3.3.1.png)

- Hecho esto en las propiedades del servidor SMTP iremos a `Acceso`-->`autenticación`-->`Todo excepto la lista...`-->`agregar` y pondremos una IP.

  ![3.4.0](./img/3.4.0.png)

  ![3.4.1](./img/3.4.1.png)

  ![3.4.2](./img/3.4.2.png)

- Luego en la conexión eligiremos `Acceso anónimo`

  ![3.5.0](./img/3.5.0.png)

  ![3.5.1](./img/3.5.1.png)

- Por último en la retransmisión eligiremos `Todos excepto ...`

  ![3.6](./img/3.6.png)

  ![3.6.1](./img/3.6.1.png)

## 2.1 Dominio para SMTP

- Para crear un dominio de nuestro servicio SMTP iremos al panel del servidor y `herramientas`-->`Administrador de Internet Information Services (IIS) 6.0`-->`SMTP`-->`Dominios`-->`Nuevo -- dominio`.

  ![3.7.2](./img/3.7.2.png)

- Eligiremos `Alias`

  ![3.7.3](./img/3.7.3.png)

- Le daremos un nombre al dominio.

  ![3.7.4](./img/3.7.4.png)

- Hecho esto quedaría así.

  ![3.7.5](./img/3.7.5.png)

- Si vamos a la ruta `c:/inetpub/mailroot` veremos que se nos ha creado unas carpetas.

  ![3.8](./img/3.8.png)

___

# 3. Cliente Windows

- Comprobamos que tenemos conexión al servidor a través del nombre de dominio que le hemos dado.

  ![4.1](./img/4.1.png)

- Descargamos el cliente *Opera Mail* para enviar correos.

## 3.1 Sin cifrado anónimo

- Lo primero que haremos será enviar un correo a una cuenta que si existe de verdad y veremos si lo recibimos.

  ![4.2.0](./img/4.2.0.png)

  ![4.2.1](./img/4.2.1.png)

- Ahora lo enviaremos a una cuenta que no existe y veremos que no se envia y se nos queda en las carpetas de SMTP en el servidor.

  ![4.3.1](./img/4.3.1.png)

  ![4.3.2](./img/4.3.2.png)

  ![4.3.3](./img/4.3.3.png)

## 3.2 Sin cifrado TLS autenticación básica.

- Para esto primero deberos ir a las propiedades del *SMTP* en el servidor.

  ![5.0](./img/5.0.png)

- En `acceso`-->`autenticación` eligiremos `autenticación básica`

  ![5.3](./img/5.3.png)

- Ahora pasaremos a comprobar que funciona con los correos, para esto debemos crear cuentas con las que el usuario este dentro de los usuarios de Active Directory y no activar la conexión segura TLS.

  ![6](./img/6.png)

- Probamos primero enviando un mensaje a un correo que no existe y veremos que se nos guarda en las carpetas de SMTP.

  ![6.0](./img/6.0.png)

  ![6.1](./img/6.1.png)

- Ahora probamos con un correo que si existe y veremos que lo recibimos.

  ![6.3](./img/6.3.png)

  ![6.4](./img/6.4.png)

## 3.3 Con cifrado TLS y autenticación básica.

- Para esto haremos lo mismo pero cuando creemos la cuenta de correo activaremos la opción `conexion segura TLS`

  ![7.0](./img/7.0.png)

- Probaremos ahora con un correo que no existe y veremos que pasa lo mismo que las otras veces que se nos envia a las carpetas de SMTP pero esta vez nos pedirá que aceptemos un mensaje de seguridad.

  ![7.1](./img/7.1.png)

  ![7.2](./img/7.2.png)

  ![7.3](./img/7.3.png)

  ![7.4](./img/7.4.png)

- Si ahora enviamos a un correo que si existe veremos que lo recibimos y en este caso no nos sale ningún mensaje de seguridad ya que lo hemos aceptado ya.

  ![7.5](./img/7.5.png)

  ![7.6](./img/7.6.png)

___
___
___
<a name="hmail"></a>

# Hmail Windows Server 2012

![portada](./img/hmail/portada.png)

___

## 1. Desinstalar SMTP

- Lo primero que haremos será desinstalar la característica SMTP, para esto iremos al panel principal --> `Administrar`-->`Quitar roles y funciones`.

  ![1.0](./img/hmail/1.0.png)

- Una vez dentro en el apartado de `características` desactivaremos `Servidor SMTP`

  ![1.3](./img/hmail/1.3.png)

  ![1.4](./img/hmail/1.4.png)

- Y por último confirmamos.

  ![1.5](./img/hmail/1.5.png)

## 2. Instalación de servidor hMailServer

- Para instalarlo lo primero será descargarlo, para esto iremos a este [enlace](https://www.hmailserver.com/donwload), y descargaremos la última versión.

  ![2.0](./img/hmail/2.0.png)

- Antes de comenzar a instalarlo activaremos una característica en el servidor llamada `.NET Framework 3.5`

  ![2.9](./img/hmail/2.9.png)


- Una vez descargado comenzaremos la instalación.

  ![2.1](./img/hmail/2.1.png)

  ![2.2](./img/hmail/2.2.png)

  ![2.3](./img/hmail/2.3.png)

  ![2.4](./img/hmail/2.4.png)

  ![2.5](./img/hmail/2.5.png)

  ![2.6](./img/hmail/2.6.png)

  ![2.7](./img/hmail/2.7.png)

  ![2.8](./img/hmail/2.8.png)

- Una vez instalado pasaremos a ejecutarlo y veremos que nos pide una contraseña que será la que hemos puesto en la instalación.

  ![2.10](./img/hmail/2.10.png)

  ![2.10.0](./img/hmail/2.10.0.png)

- Entrando en `localhost` y veremos que estaremos dentro ya del *hMailServer*

  ![2.11](./img/hmail/2.11.png)

## 3. Creación de dominios

- Dentro de *hMailServer* iremos a `Domains` y añadiremos un nuevo dominio *srd.edu* y *asir.edu*.

  ![3.0](./img/hmail/3.0.png)

  ![3.1](./img/hmail/3.1.png)

- De tal manera que al final nos quede así.

  ![3.2](./img/hmail/3.2.png)

## 4. Diagnóstico-Backup.

- Realizaremos un diagnóstico, para esto iremos la última opción llamada `utilities` --> `Diagnostics` y haremos uno por cada dominio y veremos que nos falla un par de cosas, pero en este apartado nos fijamos en el de backup.

  ![4.0](./img/hmail/4.0.png)

  ![4.1](./img/hmail/4.1.png)

- Para resolver esto iremos a la opción `utilities`-->`Backup` y eligiremos una carpeta para ello .

  ![4.2](./img/hmail/4.2.png)

- Veremos que si hacemos un nuevo diagnóstico ya no nos saldrá el error de Backup.

  ![4.3](./img/hmail/4.3.png)

  ![4.4](./img/hmail/4.4.png)

## 5. Cuentas de usuario de dominio.

- Para esto iremos a `Domains`-->`Accounts` y añadiremos una cuenta de usuario por cada dominio.

- Cuenta para asir.edu:

  ![5.0](./img/hmail/5.0.png)

- Cuenta para srd.edu: a esta le añadiremos una opción llamda `auto-reply` que su funcion sera responder automaticamente mensajes.

  ![5.2](./img/hmail/5.2.png)

## 6. Servicio DNS MX. 
