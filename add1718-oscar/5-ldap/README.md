Óscar Moreira

# Servidor LDAP - OpenSUSE

![portada](./img/portada.png)

___

# Práctica

Esta práctica consiste en crear un *servidor LDAP* en OpenSUSE con un cliente OpenSUSE.

Se crearán unos usuarios para LDAP y grupos con los que luego desde el cliente entraremos sin estar definidos en el cliente ya que están en el servidor LDAP.

___

# Máquinas

1. OpenSUSE servidor LDAP:

    - Nombre de equipo: `ldap-server05`
    - IP: `172.18.5.31`
    - DNS: `8.8.4.4`



2. OpenSUSE cliente:

    - Nombre de equipo: `ldap-client05`
    - IP: `172.18.5.32`
    - DNS: `8.8.4.4`

___
___

# Procedimiento práctica

# 1. Servidor LDAP

En esta práctica configuraremos LDAP con la herramienta *OpenLDAP*

## 1.1 Preparativos

Después de haber configurado la IP pasararemos a preparar el servidor.

En el archivo `/etc/hosts` añadiremos las siguientes lineas que veremos en la imágen, en las que añadiremos el host del servidor el del cliente y el de LDAP.

![1.1.1](./img/1.1.1.png)

## 1.2 Instalación del Servidor LDAP

 Lo primero que haremos será instalar (`yast2-auth-server`).

> Esto servirá para gestionar la configuración del servidor LDAP en yast

  ![1.2.1](./img/1.2.1.png)

El siguiente paso que haremos será configurar la autenticación:

- En Yast iremos a `Servidor de autenticación` o en inglés `authentication Server`.

  ![1.2.2](./img/1.2.2.png)

- Dentro instalaremos los paquetes: `openldap2`, `krb5-server`, `krb5-client`.

  ![1.2.3](./img/1.2.3.png)

- Seguimos y en los ajustes generales:

  - Iniciar servidor LDAP = `Si`
  - Registrar dameon SLP = `No`
  - Puerto abierto en el cortafuegos = `SI`

    ![1.2.4](./img/1.2.4.png)

- Lo siguiente será el tipo de servidor `autónomo`.

  ![1.2.5](./img/1.2.5.png)

- Configuración TLS = `No habilitar`

  ![1.2.6](./img/1.2.6.png)

- Configuración básica de la base de datos

  - Tipo de BD = `hdb`
  - DN base = `dc=oscar05,dc=curso1718`
  - DN administrador = `cn=Administrator`
  - Añadir DN base = `SI`
  - Contraseña = `SI`
  - Directorio de BD = `/var/lib/ldap`
  - Usar esta base de datos... = `si`

    ![1.2.7](./img/1.2.7.png)

- En Habilitación de Kerberos `NO` habilitaremos la autenticación.

  ![1.2.8](./img/1.2.8.png)

- Terminamos y veremos el resultado final.

  ![1.2.9](./img/1.2.9.png)

___

Comprobaciones:

- `slaptest -f /etc/openldap/slapd.conf`: comprobacón de sintaxis del fichero de configuración.

  ![1.2.10](./img/1.2.10.png)

- `systemctl status slapd`: Comprobación del estado del servicio.

  ![1.2.11](./img/1.2.11.png)

- `systemctl enable slapd`; Activar el servicio automaticamente cuando iniciemos.

  ![1.2.11.1](./img/1.2.11.1.png)

- `nmap -Pn localhost | grep -P '389|636'`: Comprobación de que es accesible a la red.

  ![1.2.12](./img/1.2.12.png)

- `slapcat`: Verificar que la base de datos esta bien.

  ![1.2.13](./img/1.2.13.png)

- Instalar herramienta `gq` y usar  para comprobar el contenido de la base de datos LDAP.

  ![1.2.14](./img/1.2.14.png)

- Comrpobaremos que tenemos las unidades : `groups` y `people`

  ![1.2.15](./img/1.2.15.png)

___

## 1.4 Creación de usuarios y grupos LDAP

- Lo primero será ir a *Yast* -/- *Gestión de usuarios y grupos*

  ![1.4.1.1](./img/1.4.1.1.png)

- Luego de esto iremos a `usuarios` y en `filtro` eligiremos `LDAP`.

  ![1.4.1.2](./img/1.4.1.2.png)

  - Aquí dentro crearemos los usuarios: `pirata21` y `pirata22`.

    ![1.4.3](./img/1.4.3.png)

- Creados los usurios pasaremos a los grupos y haremos el mismo procedimiento pero crearemos un grupo solo llamado `piratas2`.

  ![1.4.2](./img/1.4.2.png)

- Ahora usaremos la herramienta `gq` para comprobar que los usuarios y el grupo están en la base de datos *LDAP*.

  ![1.4.5](./img/1.4.5.png)

- Una vez comprobado que nos sale esa información en la herramienta `gq` pasaremos a lo siguiente.

- Ahora pasaremos a ejecutar el comando: `ldapsearch -x -L -u -t "(uid=nombre-del-usuario)"`

  > Este comando servirá para consultar en la base de datos LDAP la información del usuario con uid concreto.

  ![1.4.6](./img/1.4.6.png)

___
___

# 2. Cliente LDAP

## 2.1 Preparativos

Configurada la maquina cliente con los primeros pasos de IP, nombre de equipo, etc... pasaremos a modificar el fichero `/etc/hosts` con las lineas que veremos en la siguiente imágen en a que pondremos el host del propio cliente y el del servidor LDAP.

  ![2.1.1](./img/2.1.1.png)

### Comprobación

- `nmap -Pn ldap-serverXX | grep -P '389|636'`, Comprobaremos que el servidor LDAP es accesible desde el cliente.

  ![2.1.2.1](./img/2.1.2.1.png)

- Luego con la herramienta `gq` en el cliente en: `file/preferences/`

  ![2.1.2.2](./img/2.1.2.2.png)

- Luego iremos a `servers` y añadiremos uno nuevo y pondremos lo siguiente:

  - LDAP Host/URI = `ldap://ldap-server05`
  - Base DN = `dc=oscar05,dc=curso1718`

    ![2.1.2.3](./img/2.1.2.3.png)

- Después de esto comprobaremos que tenemos la base de datos LDAP que creamos en el servidor con sus usuarios y grupo.

  ![2.1.2.4](./img/2.1.2.4.png)

___

## 2.2 Instalar cliente LDAP.

- Instalaremos (`yast2-auth-client`), para configurar la autenticación.

  ![2.2.1](./img/2.2.1.png)

- Luego iremos a: `Yast/LDAP y cliente Kerberos`

  ![2.2.2](./img/2.2.2.png)

- Una vez dentro le daremos a `cambiar configuración`

  ![2.2.3.1](./img/2.2.3.1.png)

- Dentro de la configuración deberáquedar de esta manera y darle a probar conexión.

  ![2.2.3.2](./img/2.2.3.2.png)

___

## 2.3 Comprobación desde cliente.

- Ejecutaremos los siguientes comandos:

  ~~~
  getent passwd pirata21
  getent group piratas2
  id pirata21
  finger pirata21
  ~~~

    ![2.3.1](./img/2.3.1.png)
  ~~~
   cat /etc/passwd | grep pirata21
   cat /etc/group | grep piratas2
  ~~~
    ![2.3.2](./img/2.3.2.png)

  ~~~
  su pirata21
  su pirata22
  ~~~

    ![2.3.3](./img/2.3.3.png)  

    ![4.1](./img/4.1.png)

___

## 2.4 autenticación

Reiniciaremos para poder entrar por interfaz al cliente a un usuario de LDAP.

Al reiniciar ha dado el error siguiente:

![error_cliente_ldap](./img/error_cliente_ldap.png)

#### Solución :

1. Iniciaremos la máquina del cliente con `Knoppix Live`

2. En el fichero `/etc/nsswitch.conf` quitaremos la palabra ***ldap*** ya que se generó sola al hacer la configuración de LDAP por yast.

3.  passwd: files nis ldap shadow: files nis group: files nis ldap

4. Reiniciar MV cliente

5. Repetir configuración Yast.

___
___

Fín de la práctica.
