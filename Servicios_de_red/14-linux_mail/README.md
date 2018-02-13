Óscar Moreira Estévez

Carlos Oliva

# Instalación y configuración de un Servidor de correo en LINUX

![portada](./img/portada.png)

## 1. Instalación servicio SMTP

- Lo primero que haremos sera instalar el servidor *Postfix* siguiendo los siguientes pasos:

  ![1](./img/1_apt_install.png)

  ![2](./img/2_postfix_conf.png)

  ![3](./img/3_internet_site.png)

  ![4](./img/4_postfix_name.png)

- Ahora comprobaremos que el servicio esta corriendo.

  ![5](./img/5_postfix_status.png)

  - `netstat -utap`

    ![6](./img/6_service.png)

- En este paso haremos pruebas de envío de mensajes mediante telnet en el que seguiremos los siguientes comandos que veremos dentro de la imagen.

  - `telnet localhost 25`

    ![7](./img/7_telnet.png)

  - Iremos a la ruta `/varspool/mail`  miraremos que se reciba el correo enviado al usuario indicado.

      ![8](./img/8_check_client.png)

### 1.2 Cliente OperaMail

- Instalaremos un cliente de correo en un cliente en nuestro caso ha sido el *OperaMail*.

  ![9](./img/9_operamail.png)

- Creamos dos lineas nuevas en el fichero `/etc/hosts` en el que introduzcadmos la IP del servidor para los dns(smtp.miempresa.com y pop.miempresa.com).

  ![10](./img/10_hosts.png)

  ![11](./img/11_hosts_cli)  

- Comprobamos haciendo ping a un dns para verificar que hace conexión.

  ![12](./img/12_ping.png)

- Ahora creamos dos cuentas de usuario.

  ![13](./img/13_users_server.png)

  ![14](./img/14_users_windows.png)

- Ahora comprobaremos que funciona bien el servicio smtp.

  - De Carlos a Oscar:

    ![15](./img/15_send.png)

    ![17](./img/17_check.png)

  - De Oscar a Carlos:

    ![16](./img/16_send.png)

    ![18](./img/18_check.png)

## 2. Imap y SquirrelMail
