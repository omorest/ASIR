# Puppet

![portada](./img/portada.png)

___

# 1. Configuración

## 1.1 Máquinas virtuales

En esta práctica usaremos 3 maquinas virtuales con la siguiente configuración:

- MV1 - Master: este será quien de las ordenes a los clientes:

  - SO: OpenSUSE
  - IP: 172.18.5.100
  - Nombre equipo: master05
  - Dominio: curso1718

- MV2 - Master: este recibirá ordenes del master:

  - SO: OpenSUSE
  - IP: 172.18.5.101
  - Nombre equipo: cli1alu05
  - Dominio: curso1718

- MV3 - Master: este recibirá ordenes del master:

  - SO: Windows 10
  - IP: 172.18.5.102
  - Nombre equipo: cli2alu05

## 1.2 configuración `/etc/hosts`

En este apartado lo que haremos será configurar el fichero  `/etc/hosts` de modo que tenga el resto de los hosts para así poder obetener la resolución de nombres de todas nuestras máquinas.

- MV1 - Master OpenSUSE:

  ![1.2](./img/hosts_master.png)

- MV2 - Cliente OpenSUSE:

  -![host cliente](./img/hosts_cliente.png)

- MV3 - Cliente W10:

  ![1.2.4](./img/1.2.4.png)

  ![1.2.5](./img/1.2.5.png)

## 1.3 Comprobación de las configuraciones.

- Linux:

  ~~~
  date
  ip a
  route -n
  host www.google.es
  hostname -a
  hostname -f               # Comprobar que devuelve el valor correcto!!!
  hostname -d               # Comprobar que devuelve el valor correcto!!!
  tail -n 5 /etc/hosts
  ping master05
  ping master05.curso1718
  ping cli1alu05
  ping cli1alu05.curso1718
  ping cli2alu05
  ~~~
  - Master

    ![master hostname](./img/hostname_master.png)

  - Cliente

    ![cliente hostname](./img/hostname_cliente.png)

- Windows:

  ~~~
  date
  ipconfig
  route PRINT
  nslookup www.google.es
  ping master05
  ping master05.curso1718
  ping cli1alu05
  ping cli1alu05.curso1718
  ping cli2alu05
  ~~~

___

# 2. Instalación y configuración del servidor

> En el master

- Instalamos Puppet Master en el servidor: sudo zypper install rubygem-puppet-master

  ![2.0.1](./img/2.0.1.png)

- Ahora ejecutaremos los siguientes comandos:

  - sudo systemctl enable puppetmaster: `se iniciará automáticamente`
  - sudo systemctl start puppetmaster: `iniciamos el servicio`
  - sudo systemctl status puppetmaster: `verificamos que esta corriendo el servicio`

    ![2.0.4](./img/2.0.4.png)

- Habiendo hecho esto se nos crea el directorio `/etc/puppet/manifests`

  ![2.0.5](./img/2.0.5.png)

- Ahora crearemos los siguientes ficheros:

  ~~~
  mkdir /etc/puppet/files
  touch /etc/puppet/files/readme.txt
  mkdir /etc/puppet/manifests
  touch /etc/puppet/manifests/site.pp
  mkdir /etc/puppet/manifests/classes
  touch /etc/puppet/manifests/classes/hostlinux1.pp

  ~~~

  ![2.0.6](./img/2.0.6.png)

## 2.1 Site.pp

- Editaremos el ficero `/etc/puppet/manifests/site.pp` poniendo el siguiente contenido:

  ~~~
  import "classes/*"

  node default {
    include hostlinux1
  }
  ~~~

  ![2.2.](./img/2.2.png)     

## 2.2. Hostlinux1.pp

- En este fichero le añadiremos el siguiente contenido:

  ~~~
  class hostlinux1 {
    package { "tree": ensure => installed }
    package { "traceroute": ensure => installed }
    package { "geany": ensure => installed }
  }
  ~~~

  ![2.3.1](./img/2.3.1.png)

- Verificamos que los directorios y ficheros están bien:

  ![2.3.2](./img/2.3.2.png)

- Comprobamos que el directorio `/var/lib/puppet` tiene usuario/grupo propietario `puppet`

  ![2.3.3](./img/2.3.3.png)

- Reiniciamos el servicio y luego verificamos que esta corriendo bien:

  ![2.3.4](./img/2.3.4.png)

  ![2.3.5](./img/2.3.5.png)

- Para consultar los errores: `tail /var/log/puppet/*.log`

  - En nuestro caso no sale nada porque no tenemos ningún error.

- Abrimos el cortafuegos:

  ![2.3.6](./img/2.3.6.png)

___

# 3. Instalación y configuración cliente1

> Desde cliente1 OpenSUSE.

- Instalamos el Agente Puppet: `sudo zypper install rubygem-puppet`

  ![3.2](./img/3.2.png)

- El cliente debe saber quien es su master asi que modificaremos el fichero `/etc/puppet/puppet.conf` añadiendole dos lineas más.

  ![3.3](./img/3.3.png)

## 3.1 Comprobaciones

- Verificamos que el directorio `/var/lib/puppet` tiene usuario y grupo propietario `puppet`.

  ![3.4](./img/3.4.png)

- Para que el servicio de puppet se active automáticamente haremos: `systemctl enable puppet`

- Iniciamos con `systemctl start puppet`

- Verificamos que esta corriendo: `systemctl status puppet`

  ![3.5](./img/3.5.png)

- Para mostrar los servicios conectados a cada puerto: `netstat -ntap |grep ruby`

  ![3.6](./img/3.6.png)

- Abriremos el cortafueros para el servicio `puppet`

___

# 4. Certificados

Para que el master y el cliente se puedan comunicar y recibir órdenes el uno del otro habrá que intercambiarse los certificados.

## 4.1 Aceptar certificado.

> Desde el master05

- Como usuario root.

- Miramos si hay peticiones pendientes

  ![4.1.2](./img/4.1.2.png)

- Aceptamos al nuevo cliente

  ![4.1.3](./img/4.1.3.png)

  ![4.1.3.1](./img/4.1.3.1.png)

## 4.2 Comprobación

> Desde el cliente1

- Reiniciamos la máquina y servicio puppetmaster

- Como usuario root siguientes comandos:

  ![4.2.3.1](./img/4.2.3.1.png)

  ![4.2.3.2](./img/4.2.3.2.png)

- Comprobamos si tenemos errores.

> Veremos que no tenemos el fichero debido a que no hay errores.

  ![4.2.4](./img/4.2.4.png)

- Para comprobar que ha funcionado iniciamos el programa `geany` que es el que le hemos dado la orden de que instale.

  ![4.3](./img/4.3.png)
___

# 5. Hostlinux2.pp
> Desde el master

Esta será una configuración mas compleja que la anterior.

- Editaremos el fichero `/etc/puppet/manifests/classes/hostlinux2.pp` con el siguiente contenido:

  ![hostlinux2](./img/hostlinux2.png)
  ~~~
  class hostlinux2 {
    package { "tree": ensure => installed }
    package { "traceroute": ensure => installed }
    package { "geany": ensure => installed }

    group { "piratas": ensure => "present", }
    group { "admin": ensure => "present", }

    user { 'barbaroja':
      home => '/home/barbaroja',
      shell => '/bin/bash',
      password => 'poner-una-clave-encriptada',
      groups => ['piratas','admin','root']
    }

    file { "/home/barbaroja":
      ensure => "directory",
      owner => "barbaroja",
      group => "piratas",
      mode => 750
    }

    file { "/home/barbaroja/share":
      ensure => "directory",
      owner => "barbaroja",
      group => "piratas",
      mode => 750
    }

    file { "/home/barbaroja/share/private":
      ensure => "directory",
      owner => "barbaroja",
      group => "piratas",
      mode => 700
    }

    file { "/home/barbaroja/share/public":
      ensure => "directory",
      owner => "barbaroja",
      group => "piratas",
      mode => 755
    }
  }
  ~~~

- Luego modificaremos el fichero `site.pp`:

  ~~~
  import "classes/*"

  node default {
    include hostlinux2
  }
  ~~~

  ![5.2](./img/5.2.png)

- Ahora ejecutaremos el comando `tree` para ver que tenemos todos los ficheros bien.

  ![5.3](./img/5.3.png)

- Reiniciamos el servicio y continuamos con el cliente1.

- Ahora comprobamos que se ha aplicado todo.

  - Carpetas:
  
    ![5.4.1](./img/5.4.1.png)

  - Grupos:

    ![grupo root](./img/grupo_hotlinux2.png)

    ![Grupos](./img/grupos_hostlinux2.png)

  - Permisos:

    ![Permisos](./img/permisos_hostlinux2.png)

# 6. Configuración Puppet en Windows

> Tener las máquinas clientes con la misma hora que en el master.

## 6.1 HostWindows3.pp

> Desde el master

- Crearemos y editaremos el fichero: `/etc/puppet/manifests/classes/hostWindows3.pp`

  ~~~
  class hostWindows3 {
    file {'C:\warning.txt':
      ensure => 'present',
      content => "Hola Mundo Puppet!",
    }
  }
  ~~~

  ![6.1.3](./img/6.1.3.png)

- Ahora modificaremos el fichero `site.pp` para que pueda trabajar también con clientes Windows.

  ~~~
  import "classes/*"

  node 'cli1alu05.curso1718' {
    include hostlinux2
  }

  node 'cli2alu05' {
    include hostWindows3
  }
  ~~~

  ![6.1.4](./img/6.1.4.png)

- `tree` para verificar los cambios y que tenemos bien los ficheros.

  ![6.1.5](./img/6.1.5.png)

- Reiniciamos el servicio `puppetmaster`

- Con el comando `facter` veremos la versión de puppet que tenemos.

  ![6.1.7](./img/6.1.7.png)

## 6.2 Instalar cliente Puppet en Windows

> En el cliente Windows

- Descargamos la misma versión de Puppet que en el master.

  ![6.2.1.0](./img/6.2.1.0.png)

- Comenzamos la instalación de la siguiente manera.

  ![6.2.1.1](./img/6.2.1.1.png)

  ![6.2.1.2](./img/6.2.1.2.png)

  ![6.2.1.3](./img/6.2.1.3.png)

  ![6.2.1.4](./img/6.2.1.4.png)

  ![6.2.1.5](./img/6.2.1.5.png)

- Modificamos el fichero `puppet.conf` del cliente windows.

  ![6.2.3.4](./img/6.2.3.4.png)

- Despues de esto volveremos a aceptar certificados.

  ![6.2.3.3](./img/6.2.3.3.png)


## 6.3 Comprobar cambios.

- Iniciamos la consola puppet como administrador y ejecutamos lo siguiente.

> Aunque salgan errores veremos que todo funciona.

  - `puppet agent --configprint server`

  - `puppet agent --server master05.curso1718 --test`

      ![6.4.2](./img/6.4.2.png)

  - `facter`

      ![6.4.4](./img/6.4.4.png)

  - `puppet resource user oscar`
  - `puppet resource file c:\Users`

    ![6.4.5](./img/6.4.5.png)

- Veremos que tenemos el fichero Warning.txt

  ![6.2.001](./img/6.2.001.png)
___

# 7. Hostwindows4.pp

- Creamos y editamos el fichero `/etc/puppet/manifests/classes/hostwindows4.pp`.

   ~~~
   class hostwindows4 {
   user { 'soldado1':
     ensure => 'present',
     groups => ['Administradores'],
    }

   user { 'aldeano1':
     ensure => 'present',
     groups => ['Usuarios'],
      }
    }
   ~~~

  ![6.5](./img/6.5.png)

- Luego de esto editaremos el fichero `site.pp`

  ![6.5.1](./img/6.5.1.png)

- Ahora en el cliente ejecutaremos el programa `run agent puppet` para aplicarlos cambios.

  ![6.6](./img/6.6.png)

- Vemos quenos ha creado lo que le hemos ordenado.

  ![6.7](./img/6.7.png)

___

# 8. Hostalumno5.pp

- Creamos y editamos el fichero : `/etc/puppet/manifests/classes/hostalumno5.pp`.

  ![6.3.0](./img/6.3.0.png)

- Editamos el fichero `site.pp`.

  ![6.3.1](./img/6.3.1.png)

- Ejetuamos el programa `run agent puppet`

  ![6.3.2](./img/6.3.2.png)

- Veremos que se han creado los usuarios y grupos

  ![6.3.3](./img/6.3.3.png)

___

# 9. Para probar: Fichero readme.txt

Los ficheros que se guardan en `/etc/puppet/files` se pueden descargar desde el resto de máquinas cliente puppet.

-  Contenido para readme.txt: "¡Al abordaje!".
- Ejemplo de configuración puppet para descargar fichero:

~~~
file {  '/opt/readme.txt' :
       source => 'puppet:///files/readme.txt',
}
~~~

> Este apartado no lo he conseguido hacer.


___
___

Fín de la práctica
