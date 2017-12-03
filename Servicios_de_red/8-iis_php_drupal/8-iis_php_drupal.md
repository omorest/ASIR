# Informe IIS - Servidor Web avanzado - PHP, MySQL, phpMyAdmin, FTP y Drupal

![portada](./img/portada.jpg)

___

# Prácticas

### Parte 1:
- La primera parte de la práctica consistirá en crear un servidor web con soporte PHP, acceso FTP y gestor de bases de datos y phpMyAdmin.

### Parte 2:
### Parte 3:

___
___

# 1. Parte 1

## 1.0 IIS Windows Server 2012 V

En este apartado instalaremos y configuraremos todas las características necesarias para nuestro servidor de tal forma que luego podremos trabajar desde el cliente y configurar desde el cliente.

## 1.1 Instalación PHP

- Lo primero que haremos será descargar PHP la versión 5.3.8

  ![php_download](./img/1/1_php_download.png)

- Descargado lo siguiente sera instalarlo y seguiremos los pasos que veremos en las imágenes siguientes.

  ![php_install](./img/1/2_php_install_1.png)

  ![php_install](./img/1/2_php_install_2.png)

  ![php_install](./img/1/2_php_install_3.png)

  ![php_install](./img/1/2_php_install_4.png)

  ![php_install](./img/1/2_php_install_5.png)

- Ahora añadiremos la carácterística llamada CGI en el servidor.

  ![cgi](./img/1/3_add_cgi.png)

  ![cgi](./img/1/4_cgi_added.png)

- Una vez instalado el CGI pasaremos a crear nuestro sitio web y lo primero sera crear la carpeta llamada *cms*

  ![cms folder](./img/1/6_cms_folder.png)

- Dentro de esta carpeta crearemos un fichero *index.php* con el código siguiente dentro de él.

  ~~~
  <?php phpinfo(); ?>
  ~~~

  ![cms index](./img/1/6_cms_index.png)

- Crearemos un alias.

  ![new alias](./img/1/8_new_alias.png)

- Despuñes de esto iremos a *IIS* y crearemos el sitio web *cms.miepresa.com*.

  ![new site](./img/1/7_new_site.png)

- Por último en el sitio web en *IIS* en documentos predeterminados pondremos el *index.php* al principio.

  ![php up](./img/1/9_admit_php.png)

- Ahora ya comprobaremso que entrando en nuestro sitio web en un navegador nos saldrá el contanido de PHP.

  ![php version](./img/1/10_php_version.png)

___

## 1.2 Instalación MySQL

Para instalar el *MySQL* seguiremos los siguientes pasos:
- Primero iremos a este [enlace](https://dev.mysql.com/donwloads/installer) y descargamos la segunda opción de 376.3M (instalador completo).

  ![download_mysql](./img/1/11_mysql_download.png)

- Una vez descargado seguiremos los siguientes pasos para la instalación.

  ![mysql](./img/1/12_mysql_installer_1.png)

  ![mysql](./img/1/12_mysql_installer_2.png)

  ![mysql](./img/1/13_mysql_config_1.png)

  ![mysql](./img/1/13_mysql_config_2.png)

  ![mysql](./img/1/13_mysql_config_3.png)

  ![mysql](./img/1/13_mysql_config_4.png)

  ![mysql](./img/1/13_mysql_config_5.png)

- Y siguiente hasta acabar.

## 1.3 phpMyAdmin

- Descargaremos phpMyAdmin en este [enlace](http://www.phpmyadmin.net)

  ![pma](./img/1/14_pma_download.png)

- Crearemos una carpeta llamada phpmyadmin en *miempresa* con todos los ficheros.

  ![pma](./img/1/14_pma_folder.png)

- Ahora creamos un nuevo dominio para phpmyadmin

  ![domini pma](./img/1/16_newalias_myadmin.png)

- Creado el dominio crearemos el sitio web en *IIS*

  ![web pma](./img/1/15_newsite_myadmin.png)

- Ahora verificamos si entrando a la web nos sale la página.

  ![pma check](./img/1/17_check_result.png)

___
___

# Parte 2
