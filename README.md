# Web Scraping de IMDb

## 📋 Objetivo
El objetivo de este proyecto es extraer información detallada y estructurada desde la página web de IMDb, la base de datos más popular de películas, programas de televisión, actores y mucho más. Este proyecto tiene como propósito analizar, visualizar y proporcionar datos útiles sobre la industria del cine y la televisión.

## 🛠️ Funcionalidades
- **Cargar Datos:** Extraer los datos de IMBd con BeautifulSoup4 y almacenarlos en un indice creado con Whoosh 
- **Listar Datos:** Listar todos los datos almacenados en el indice ordenados por distintos parametros seleccionables.
- **Buscar:** Funcion para buscar documentos especificos en el indice por título, año de lanzamiento o edad recomendada de visualización.  
- **Visualización:** Generación de gráficos para mostrar los datos extraídos y analizarlos con facilidad. 

## 📂 Estructura del Proyecto
- **Carpeta IMBd_web_Scrapping:** carpeta principal del proyecto 
    - **settings.py:**  se definen las rutas y configuraciones del proyecto 
    - **urls.py:** donde se vinculan las rutas y las vistas del proyecto.

- **Carpeta home:** carpeta donde se contiene la aplicación
    - **scraper_util.py:** archivo que se ocupa del scrapping, contiene todas las funciones que se ocupan de extraer los datos de la página de IMBd
    - **whoosh_util.py:** archivo que se ocupa de todo lo relacionado con los indice whoosh, este archivo contiene las funciones que declaran el esquema, crean el indices, añaden datos o extraen datos del mismo. 
    - **Carpeta templates:** carpeta donde se encuentran todas las plantillas
    - **views.py:** archivo donde se definen todas las vistas de la aplicación.

- **Carpeta static:** carpeta donde se encuentran todos los archivos estaticos, dentro de esta se encuenta los archivo css, para los estilos de las plantillas.

- **requirements.txt:** archivo donde se recogen todos los requisitos para que el proyecto se ejecute correctamente

## 🛠️ Herramientas Usadas
El proyecto hace uso de un conjunto de herramientas y bibliotecas para lograr sus objetivos de scraping, análisis, visualización de datos y creación de la interfaz web. A continuación, se detallan:

- **[Django](https://www.djangoproject.com/):** Framework web de alto nivel que permite la creación de aplicaciones robustas, flexibles y seguras. Es el framework sobre el que se cimienta el proyecto.

- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/):** Biblioteca de Python para la extracción de datos de archivos HTML y XML. Se utiliza para realizar el web scraping de las páginas de IMDb y procesar la información de manera estructurada.

- **[Whoosh](https://whoosh.readthedocs.io/):** Motor de búsqueda escrito en Python. Se utiliza para indexar los datos extraídos de IMDb, permitiendo realizar consultas rápidas y eficientes sobre la información.

- **[Python](https://www.python.org/):** Lenguaje de programación principal utilizado para la lógica del proyecto, incluyendo el web scraping y procesamiento de datos.

- **[HTML/CSS](https://developer.mozilla.org/en-US/docs/Web/HTML):** Lenguajes de marcado y estilo usados para crear la estructura y diseño de la interfaz web del proyecto, ofreciendo una experiencia visual clara y organizada.

- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript):** Lenguaje de programación del lado del cliente, utilizado para generar gráficos dinámicos e interactivos mediante la biblioteca Chart.js.

- **[Chart.js](https://www.chartjs.org/):** Biblioteca JavaScript para la creación de gráficos interactivos y visualmente atractivos, utilizada para representar visualmente los datos extraídos y analizados.

## 📖 Manual de Usuario

Este manual proporciona una guía sencilla para utilizar el proyecto y explorar los datos extraídos de IMDb.

---

### **1. Requisitos Previos**
Antes de utilizar el proyecto, asegúrate de tener instalado:
- Python 3.8 o superior.
- Acceso a internet para realizar el scraping de IMDb (o datos locales si el scraping ya se realizó).

---

### **2. Instalación**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JuaniniGC/IMBd_web_scrapping_app.git
   cd IMBd_web_scrapping
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias: 
    ```bash
   pip install -r requirements.txt
   ```

4. Inicia el servidor de desarrollo:
    ```bash
   python manage.py runserver
   ```

5. Abre tu navegador y navega a http://127.0.0.1:8000. 🚀

