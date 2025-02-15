# Scraping_LP

Proyecto de Análisis de datos para la materia ***Lenguajes de Programación***. La data recolectada son ofertas de trabajo extraidas utilizando Scraping en distintas plataformas de empleo.

## Requisitos

- Python 3.7 o superior
- Ruby 3.3.7 o superior
  
## Fase de Extracción de Datos (Ruby)

### Gemas Utilizadas

- httparty
- nokogiri
- csv
- fileutils

### Descripción

El script **Scraping.rb** utiliza las clases de la carpeta Scrapers para generar una secuencia de extracción de datos. 

- `/Scrapers` :Cada clase se encarga de la extracción de datos en una página en específico y define su propio limite de páginas a utilizar como los selectores que va a buscar. 
Cada objeto recibe como parametro una ***url*** y un ***archivo CSV*** donde buscar la información y donde guardarla, respectivamente.
- `/Clases`   :Contiene los archivos que definen como están estructuradas las ofertas de trabajo, cada archivo define su propio metodo para guardarse dentro del archivo CSV que le corresponde.
- `/datosCSV` :Los archivos .csv con las ofertas extraídas de cada página web.

### Uso

1. Ejecuta el script `Scraping.rb` con el comando `ruby .\Scraping.rb`
   
   ![Ejecución desde la terminal](readme_Material/uso_ScrapingRB.png)

2. El programa cargará los datos en los archivos .csv, esperar hasta que finalice.


## Fase de Pre procesamiento y Visualización (Python)

### Librerias Utilizadas

- pandas
- matplotlib.pyplot
- PdfPages
- re
- Counter

### Descripción

El script **generar_reporte.py** utiliza los archivos de la carpeta Previsualizacion para generar un .pdf con todos los gráficos de las respuestas a las preguntas del análisis utilizando la información recolectada en la fase de Scraping. 

- `/Previsualizacion` :Cada archivo contiene el procesamiento de datos para responder una pregunta de las 9 que se plantearon. Utilizando pandas para manejar la información estructurada y matplotlib para graficar.

### Uso

1. Ejecuta el script `generar_reporte.py` con el comando `python .\generar_reporte.py`
   
   ![Ejecución desde la terminal](readme_Material/uso_ScrapingRB.png)

2. El programa generará el reporte, esperar hasta que finalice.

## Autor

- [Daniel Villamar].

## Colaboradores

- [Alex Peñafiel].
- [Ronald Gaibor].
