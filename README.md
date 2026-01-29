# 📰 Microservicio de Extracción Noticias

**Componente del Trabajo de Fin de Máster (TFM)** > *Máster en Ingeniería de Software y Sistemas Informáticos (MSSI)*

Microservicio constuido con **FastAPI** para la extracción automatizada de titulares y resúmenes de prensa global mediante el agregador Google News (`GNews`).

## 🛠️ Stack 
El microservicio está desarrollado con las siguientes tecnologías y librerías clave:

* `FastAPI`: Framework principal utilizado para construir la API.
* `uvicorn`: Servidor ASGI de alta velocidad encargado de ejecutar la aplicación.
* `pydantic`: Utilizado para la validación de datos y la gestión de esquemas mediante modelos de Python.
* `gnews`: Librería encargada de la interfaz con el agregador Google News.
* `py-eureka-client`: Cliente para la integración con **Netflix Eureka**.

## 🌐 Endpoints

### Extracción de noticias

`GET /news/{company}`

Consulta las menciones en prensa de los últimos siete días sobre una entidad. Devuleve una colección `articles` donde cada noticia contiene:

* `title`: Titular de la noticia.
* `descripction`: Breve extracto o resumen del contenido.
* `published_date`: Fecha de publicación.
* `url`: Enlace directo a la fuente original de la noticia.Fecha de publicación.
* `source`: Nombre del medio o plataforma que publica la información.

## ⚡ Ejecución

Navega hasta el directorio raíz del proyecto y ejecuta el siguiente comando en tu terminal:

```bash
docker compose up --build -d
```
Una vez levantado el contenedor, la API estará disponible en el puerto `8081`. Puedes verificar el funcionamiento realizando peticiones a través de tu navegador, cURL o Postman:

| Endpoint | URL Ejemplo |
| :--- | :--- |
| Extracción de noticias | `http://127.0.0.1:8082/news/Apple` |

### 📂 Estructura del Proyecto

```bash
.
├── docker-compose.yml         # Orquestación de servicios
├── Dockerfile                 # Configuración de la imagen Docker
├── main.py                    # Punto de entrada de la API (FastAPI)
├── model.py                   # Esquemas Pydantic para noticias
├── README.md                  # Documentación del proyecto
├── requirements.txt           # Dependencias del proyecto
└── search_news.py           # Lógica de extracción (GNews API)
```

