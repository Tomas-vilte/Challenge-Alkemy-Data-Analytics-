## Challenge-Alkemy-Data-Analytics-


#### Primero cree y ejecute un virtual enviroment:
   - `python -m venv venv`

#### Descargue las dependencias necesarias para correr el programa:
   - `pip -r install requirements.txt`

#### Despues configure la conexion a la base de datos desde un archivo .ini
[settings]
DB_CONNSTR = postgresql+psycopg2://postgres:postgres@localhost/data_analytics

   MUSEO_URL = https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09fresource4207def0-2ff7-41d5-9095-d42ae8207a5ddownloadmuseos_datosabiertoscsv
   CINES_URL = https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv
   BIBLIOTECAS_URL = https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-
*El archivo .ini también contiene la configuración de las urls de museos, cines, bilbiotecas

### Investigación de datos
#### Puede encontrar la investigación exploratoria de datos en el jupyter notebook

### Creacion de la base de datos
#### Puede crear la base de datos ejecutando

#### python script.py

#### Este script leerá todos los archivos en /src/sql/ y ejecutará el script sql en ellos para crear cada tabla

### Correr ETL

#### Primero debe crear un archivo settings.ini. Use settings.ini como referencia, también puede establecer las variables como variables de entorno haciendo

#### export DB_CONNSTR = value
#### export MUSEO_URL = value
#### export CINES_URL = value
#### export BIBLIOTECAS_URL = value

#### Donde value es el valor correcto que necesita

#### Para ejecutar el etl usando el comando

#### python main.py --date 2022-08-02