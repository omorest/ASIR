Óscar Moreira 2º ASIR

Carlos Javier Oliva 2º ASIR
___
# DNS Linux Bind9

![portada](./img/portada.png)

___
___

# Enunciado práctica

Realizar la instalación y configuración de un servidor DNS bind9 en una máquina Linux. Se piden las siguientes acciones de configuración y prueba del funcionamiento del servicio:

- Indicar a Linux que el servidor DNS es él mismo (/etc/resolv.conf)
- Configurar servidor como caché DNS (/etc/bind/named.conf.options) con reenviadores de DNS con DNS públicos (p.e.: 8.8.8.8 y 80.58.61.250).
- Comprobar resolución de nombres externos, tanto desde el servidor como desde un cliente al que le preste servicio DNS.
- Configurar como DNS maestro instalando un dominio ficticio (tu empresa virtual) y añadiendo configuración para búsquedas de zona directa y zona inversa (/etc/bind/named.conf.local)
- Crear un archivo de búsqueda directa y otro de búsqueda inversa, similares a los que se muestran en el manual, con los registros que consideres oportunos. Utiliza la configuración básica incluida en los archivos db.local (directa) y db.127 (inversa).
- Comprobar que se resuelven los nombres desde la consola del servidor.
- Comprobar desde la consola del cliente que se resuelven correctamente los nombres dados de alta en el servidor (aunque en algunos casos, si se trata de direcciones ficticias, no se obtenga respuesta).
- Investigación (para nota): Clona la máquina con el servidor bind9 instalado y configura el nuevo linux para que bind9 se comporte como un servidor esclavo (slave) del principal (master). Comprueba el funcionamiento entre maestro, esclavo y cliente.

___
___

# 1. Práctica

## 1.1 Instalación Bind9 y configuración servidor

> En el servidor.

___

### Instalación

- Lo primero que haremos será instalar ***bind9*** en el servidor:

  ~~~console
  sudo apt-get install bind9
  ~~~

  ![bind9](./img/1_install_bind9.png)

___

### Configuración

- Una vez instalado tener en cuenta que debemos tener una IP estática en el servidor.
Cuando la cambiemos comprobaremos con el comando: `ifconfig`.

  - Como veremos nuesta IP es estática y es la `172.18.6.1` para el servidor.

    ![ip estatica](./img/2_ip_static.png)

- Cuando ya tengamos la IP configurada estáticamente modificaremos el archivo en la ruta `/etc/resolv.conf` en el que le pondremos nuestra IP como *nameserver*.

  ![resolv.conf](./img/3_resolv_server.png)

#### Reenviadores

- Seguiremos con la configuración de los reenviadores en la que tendremos que ir al archivo en la ruta: `/etc/bind/name.conf.options` , y en ***forwarders*** pondremos los reenviadores que nosotros queramos, en nuestro caso usamos los de google.

  ![reenviadores](./img/4_forwarders.png)

___

## 1.2 Configuración cliente

> En el cliente.

- El primer paso que haremos en el cliente será ponerle como *dns* la IP de nuestro servidor.

  ![ipdnsserver](./img/5_ip_client.png)

- Luego iremos también al archivo resolv.conf en la ruta: `/etc/resolv.conf` y pondremos como *nameserver* la IP de nuestro servidor.

  ![resolv.confclient](./img/5_resolv_client.png)
