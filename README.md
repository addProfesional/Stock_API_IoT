Proyecto de IoT

En esta primera etapa, se define la estructura general que tendrá el proyecto tanto para la estructura de carpetas como la de las rutas que serán los endpoints que se usarán.

Iré haciendo cambios conforme pase el tiempo:

Proyecto 'Stock API IoT'
Tecnología usada: HTTP

Genmerar archivo de dependencias (dentro de ambiente virtual):

pip freeze > dependencias

Instalación y montaje:

1. Clonar proyecto:
git clone https://github....

2. Instalar:

sudo apt-get install pkg-config

sudo apt-get install libmysqlclient-dev

1. Crear un entorno virtual nuevo:

Linux/MacOs:

cd Stock_API_IoT/

virtualenv venv

source venv/bin/activate

pip install -r "dependencias.txt"

Listar paquetes instalados:

pip list


Windows

cd Stock_API_IoT/

py -3 -m venv .venv

.venv\Scripts\activate