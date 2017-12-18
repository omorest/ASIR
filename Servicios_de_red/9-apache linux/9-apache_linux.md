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

## Crear hosts virtuales.

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

## Sitios web seguros (SSL)
