# Apache Linux

![portada](./img/portada.jpg)

___
# Explicación práctica

Esta práctica consistirá en instalar y configurar en Linux los servicios: `Apache`,`PHP`, `MySQL`, `phpMyAdmin` y también haremos configuraciones de acceso a carpetas privadas y configuraciones *SSL*.

 ___
 ___

# Práctica

## 1. Apache

- Lo primero que haremos sera instalar *Apache* : `sudo apt-get install apache2`

  ![1_apache](./img/1_install_apache.png)

- Ahora si vamos al navegador y entramos en `localhost` veremos que nos saldrá el index que se creo en `/var/www/` al instalar *Apache*.

  ![2-works](./img/2_it_works.png)

- Añadimos en `/etc/hosts` la IP con el nombre de *www.,iempresa.com*.

  ![3-hosts](./img/3_hosts.png)

___

## 2. PHP

- Instalamos PHP: `sudo apt-get insall php`

  ![php install](./img/4_php.png)

- Ahora instalaremos las librerias de *Apache* para *PHP*: `sudo apt-ger install libapache2-mod-php`.

  ![lib apache](./img/5_librerias.png)

- Después de esto crearemos un *index.php* en `/var/www/html`.

  ![index.php](./img/6_index.php.png)

- Ahora veremos que si entramos en *www.miempresa.com* nos saldra al index de *PHP*.

  ![php info](./img/7_php_info.png)

___

## 3. Crear hosts virtuales.

En este apartada crearemos sitios web que configuraremos con apache2.

- Lo priemro que haremos será crear el virtual host de *www.empleados.miempresa.com* para esto iremos a la ruta `/etc/apache2/sites-available/` y crearemos un fichero que llamaremos ***empleados.conf***.

  ![8-empelados.conf](./img/8_empleados.conf.png)

- Luego iremos al fichero `/etc/hosts` y lo añadiremos.

  ![9-hosts](./img/9_hosts.png)

- Después de esto iremos a la ruta `/var/www/` y crearemos una carpeta llamada empleados y dentro un *index.html*.

  ![10-INDEX.HTML](./img/10_index.png)

- Ahora comprobaremos que el sitio web esta bien creado y que podemos acceder a la página.

  ![11-result](./img/11_result.png)

___

## 4. Sitios web seguros (SSL)

Ahora pasaremos a crear sitios web pero en este caso con certifiacion *SSL*

- Una vez se instala *Apache* también se instala *SSL*.

- Pasaremos a generar un certificado autofirmado. Ejecutaremos los siguientes comandos:

  ~~~

    - openssl genrsa -des3 -out server.key 1024
    - openssl rsa -in server.key -out server.pem
    - openssl req -new -key server.key -out server.csr
    - openssl x509 -req -days 360 -in server.csr -signkey server.key -out server.crt

  ~~~

  ![12-serverkey](./img/12_server.key.png)

  ![13-rsa-key](./img/13_rsa_key.png)

  ![14-req-new-key](./img/14_req_new_key.png)

  ![15-days](./img/15_days.png)

- Ahora iremos al la ruta `/etc/apache2/sites-available/` y crearemos el virtual host `pagos.conf` con susconfiguración *SSL*.

  ![16-sslpagos](./img/16_ssl.png)

  ![17-server-pagos](./img/17_server_pagos.png)

- Después de esto iremos a la ruta `/var/www/` y crearemos una carpeta llamada pagos en la que crearemos un *index.html*

  ![19-index-pagos](./img/19_index_pagos.png)

- Hecho todo esto lo añadiremos el nombre a `/etc/hosts`

  ![20-pagos-hots](./img/20_pagos_on_hosts.png)

- Cuando acabemos de configurar todo ejecutaremos el comando: `sudo a2enmod ssl` que sera el módulo que habilite el *SSL* en *Apache*.

  ![21-a2enmod](./img/21_a2enmod.png)

- Ahora verificamos que funciona la página.

  ![21-result-pagos](./img/21_pagos_result.pmg)

___

## 5. Acceso a carpetas privadas.
