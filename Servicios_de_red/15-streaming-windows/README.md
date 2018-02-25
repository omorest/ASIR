Oscar Moreira

Carlos Oliva

# 1. Instalación y configuración de un Seridor Multimedia - Smooth Streaming

![portada1](./img/portada1.jpg)

___

## 1.1 Paso a Paso

- Lo primero que haremos será descargar *** IIS Media Service*** que será nuestro soporte de streaming para el Servidor Web IIS.

- Para descargarlo iremos a este [enlace](http://www.microsoft.com/es-es/download/details.aspx?id=27955) y lo instalamos con las opciones por defecto.

  ![1](./img/1.png)

  ![2](./img/2.png)

- Ahora comprobamos que en la herramienta de IIS tendremos el apartado de Servicio multimedia.

  ![3](./img/3.png)

- Hecho esto descargamos unos ejemplo de multimedia para su emisión en streaming.

  ![5](./img/5.png)

  ![8](./img/8.png)

- Luego de esto creamos un dominio nuevo por cada fichero multimedia en neustro caso creamos 2.

  ![4](./img/4.png)

- Hecho los dominios pasaremos a crear el sitio web en *IIS*.

  ![9](./img/9.png.png)
  ![10](./img/10.png)

- A cada sitio les indicamos cual será su ruta de acceso física. Esta será la ruta directa a la carpeta del video.

  ![11](./img/11.png)

  ![12](./img/12.png)

- Ahora descargamos y descomprimimos el cliente de reproducción *SmoothMediaPlayer*.

- Luego al descomprimirlo nos saldrán estos dicheros.

  ![14](./img/14.png)

- Ahora el fichero comprimido lo descomprimimos en la carpeta de cada video.

  ![15](./img/15.png)

  ![16](./img/16.png)

- Luego al *html* lo llamamos *index.html* en cada carpeta.

  ![17](./img/17.png)

- Dentro del fichero le indicamos la ruta al video.

  ![18](./img/18.png)

- Entramos en un navegador en la ruta del dominio creado y comenzamos a instalar el Silverlight.

  ![19](./img/19.png)

  ![20](./img/20.png)

### Comprobación

- Ahora comprobamos que ha funcionado tanto en el cliente como en el servidor desde un navegador.

  - Desde Servidor.

    ![22](./img/22.png)

    ![23](./img/23.png)

  - Desde Cliente.

    ![24](./img/24.png)

    ![25](./img/25.png)

## Presentaciones de Transmisión por secuencia.

![26](./img/26.png)

![27](./img/27.png)
