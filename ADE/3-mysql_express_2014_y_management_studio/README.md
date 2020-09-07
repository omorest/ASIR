Óscar Moreira 2º ASIR

# SQL Server express y Management Studio

![portada](./img/portada.png)

___

## SQL Server 2014

### Instalación

- Lo primero que haremos sera ir a este [enlace](https://www.microsoft.com/es-es/download/details.aspx?id=42299) .

- Una vez dentro descargaremos la versión avanzada de 64 bits.

  ![1.1](./img/1.1.png)

- Cuando este descargado lo ejecutaremos para iniciar la instalación.

- Luego nos saldrá un mensaje refiriendose al directorio donde se van a extraer los ficheros y le damos aceptar.

  ![1.3](./img/1.3.png)

- Cuando esto finalize ya tendremos el *centro de instalación de SQL server*.

  ![1.5.0](./img/1.5.0.png)

- Aquí dentro iniciaremos una nueva instalación.

- Seguiremos los siguientes pasos:

  1. Aceptamos los *términos de licencia*.

      ![1.5.1](./img/1.5.1.png)

  2. Pasaremos a *reglas globales* y veremos que nos pedirá reiniciar el equipo.

      ![1.5.2](./img/1.5.2.png)

  3. Una vez reiniciado volveremos a entrar en el *centro de instalación de SQL Server* e iniciamos una nueva instalación de nuevo y veremos que hemos pasado al siguiente paso.

  4. *Microsoft Update* lo dejaremos como esta.

      ![1.5.3](./img/1.5.3.png)

  5. El siguiente paso nos irá hasta la *selección de características* donde lo dejaremos por defecto.

      ![1.5.4](./img/1.5.4.png)

  6. Seguiremos por la *configuración de instancia* que lo dejaremos por defecto también.

      ![1.5.5](./img/1.5.5.png)

  7. Seguido de la *configuración del servidor* lo dejaremos igual.

      ![1.5.6](./img/1.5.6.png)

  8. En este nuevo paso de *configuración del Motor de Base de datos* cambiaremos el modo de autenticación, lo pondremos como ***modo mixto*** en el que le pondremos la contraseña al usuario administrador (sa).

      ![1.5.7](./img/1.5.7.png)

  9. Cuando demos en *siguiente* empezará la instalación.

      ![1.5.8](./img/1.5.8.png)

  10. Una vez esto acabe y estemos en *operación completada* verificamos que todas las características estan en verde y ya podremos cerrarlo.

      ![1.5.9](./img/1.5.9.png)

___
___

## SQL Server Management Studio

### Instalación

- Primero éntraremos en este [enlace](https://docs.microsoft.com/es-es/sql/ssms/download-sql-server-management-studio-ssms) para ir a descargar el instalador.

- Nos llevará a una página en la que descargaremos el primero, no nos hacen falta los paquetes.

  ![2.0](./img/2.0.png)

- Una vez descargado lo ejecutamos y le daremos a *install* en la ventana que nos sale.

  ![2.1](./img/2.1.png)

- Se empezará a instalar, esto puede tardar un rato.

  ![2.2](./img/2.2.png)

- Cuando esto acabe lo podremos abrir y ver que funciona.
___
___

## Comprobaciones

### 1. Acceso local

Para cmprobar en local abriremos una conexión y entraremos con el nombre de nuestro equipo que esta antes de la barra \*\ , y con el modo *autenticación de windows*.

  ![3.0](./img/3.0.png)

Una vez detro veremos que tenemos las bases de datos locales.

  ![3.1](./img/3.1.png)

Con esto hemos comprabado el acceso local.

___

### Acceso remoto

#### Configuración remota.

1. Dentro de la base en ***Management Studio*** clicaremos botón derecho en en el equipo e iremos a las propiedades.

    - Dentro de esto iremos a **seguridad** y verifica que la autenticación está en  ***SQL Server y modo de autenticación de Windows***. SQL Server y modo de autenticación de Windows***.

      ![3.2](./img/3.2.png)

    - Luego iremos a **conexiones** y verificar que en *conexiones de servidor remoto* esta activado. esta activado. esta activado. esta activado.

      ![3.3](./img/3.3.png)


2. Después de todo esto  iremos al ***administrador de configuración de SQL Server 2014***

    ![3.4](./img/3.4.png)

    - Dentro de *servicios de SQL Server* tener en ejecución ***SQL Server Browser*** y el resto como la imagen:

        ![3.5](./img/3.5.png)

    - Luego en *configuración de SQL Native client* en *protocolos de cliente* tener habilidado el ***TCP/IP*** y lo demás también como en la imágen

        ![3.6](./img/3.6.png)

    - Y por último en *configuración de red SQL Server* en *protocolos de SQLEXPRESS* habilitar el ***TCP/IP*** y lo demas igual a la foto.

        ![3.7](./img/3.7.png)

    - Después ya podremos cerrarlo.

- Ahora iremos a ***Management Studio*** entraremos en el servidir y clicando botón drecho en él, le daremos a `reiniciar` sí cargaremos toda la configuración hecha.

    ![3.8](./img/3.8.png)

___

### Probando conexión remota

1. Probando conexión a mi servidor desde el PC de *Carlos Oliva*.

    - Entró poniendo mi IP y en modo de autentcación SQL , con el usuario administrador y contraseña.

    - Vemos que una vez dentro sale la ip a la que esta conectado en este caso mi PC y sus bases de datos.

      ![4.1](./img/4.1.png)

2. Probando conexión de mi PC en ***Management Studio*** al servidor de **Carlos Oliva**

    - Haremos el mismo proceso de **Carlos** pero en este caso yo pondré su IP y veremos que funciona correctamente.

      ![4.0](./img/4.0.png)

___
___

Fin de la práctica.
