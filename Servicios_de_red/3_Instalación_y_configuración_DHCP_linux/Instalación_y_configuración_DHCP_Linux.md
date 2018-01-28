Óscar Moreira 2ºASIR

# Instalación y configuración DHCP Linux

![portada](./img/portada.png)

___

Esta práctica consistirá en crear y configurar (Creación de ámbitos,
reservas, exclusiones, etc..) el servicio *DHCP* en *Ubuntu 16.04*
para que nuestro cliente *Ubuntu* obtenga ip automáticamente.

___

Entrega de la práctica:

- Crear informe explicativo.
- Detallar los pasos realizados incluyendo imágenes.

## 1. Máquinas necesarias

Usaremos máquinas ya creadas y preparadas de la práctica anterior. [Instalación y configuración de máquinas](https://github.com/oscarmoreira11/ASIR/blob/master/Servicios_de_red/1-Instalaci%C3%B3n_y_configuraci%C3%B3n_de_m%C3%A1quinas/Instalacion_y_configuracion_de_maquinas.md)

- Ubuntu 16.04 (servidor)
- Ubuntu16.04 (cliente)

___

___

## 2. Instalación DHCP y configuración

- Nuestro primer paso será descargar el **isc-dhcp-server** con el siguiente comando:

  ~~~
  sudo apt-get install isc-dhcp-server
  ~~~

    ![1.0](./img/1.0.png)

- Después de esto iremos al fichero de configuración dhcp `/etc/dhcp/dhcpd.conf`
 para modificarlo.

    ![1.1](./img/1.1.png)

___

### 2.1 Ámbito nuevo

- En este le pondremos la red a la que va a pertenecer y el rango en el que
queremos tener nuestras **ips** para los clientes. Hemos excluido las 4 primeras
para otros posibles servidores, o dns, etc..

    ![1.2](./img/1.2.png)

- Una vez hecho esto iremos al cliente y ejecutaremos **ifconfig** y asi nos saldrá
información de la ip que tengamos.

    ![1.1](./img/1.2.1.png)

- Vemos que ha cogido a partir de la `172.18.5.21` como hemos puesto en el fichero de
configuración
___

### 2.2 Configuración DNS y puerta de enlace

- El siguiente paso sera ir de nuevo al fichero de configuración y añadirle
dos líneas mas en las que le indicaremos la puerta de enlace (option routers)
y el dns (option domain-name-servers).

    ![1.3](./img/1.3.png)

- Volveremos hacer un **ifconfig** en la máquina cliente y veremos que todo siue correcto.

    ![1.3.1](./img/1.3.1.png)

___

### 2.3 Reserva de IP
Lo siguiente que haremos sera crear reservas para clientes.

- Seguiremos en la configuración en el fichero `/etc/dhcp/dhcpd.conf` .

- Antes de las reservas tendremos que comentar 3 lineas del fichero que serán
las siguientes:

    ![1.4.1](./img/1.4.1.png)

    ![1.4.2](./img/1.4.2.png)

- Ahora en este tendremos que indicarle la mac del host cliente con la IP que queremos darle
 y su puerta de enlace.

     ![1.4](./img/1.4.png)

- Luego de esto volveremos a la máquina cliente en la que haremos otro `ifconfig` y veremos que
nos dará la IP que le hemos reservado a ese pc.

    ![1.4.3](./img/1.4.3.png)

___

### 2.4 Opciones necesarias

- En este caso las opciones que he puesto han sido el ***tiempo de alquiler*** y el
*** tiempo máximo de alquiler*** para que sea el adecuado para ese ámbito.

    ![1.6](./img/1.6.png)

- Otra opción que he puesto ha sido el ***tiempo de alquiler*** y el ***tiempo máximo de alquiler***
pero por defecto para cualquier dispositivo que si no coge el que está en el ámbito cogerá este.

- Simplemente hay que ponerlo por fuera de todo.

    ![1.7](./img/1.7.png)

- Resultado final del fichero de configuración.

    ![1.8](./img/1.8.png)

___
___

Fín de la práctica.
