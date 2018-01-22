Óscar Moreira Estévez

# SMTP - Windows Server 2012

![portada](./img/portada.png)

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
