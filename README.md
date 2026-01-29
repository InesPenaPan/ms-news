# 📰 Microservicio de Extracción Noticias

**Componente del Trabajo de Fin de Máster (TFM)** > *Máster en Ingeniería de Software y Sistemas Informáticos (MSSI)*

Microservicio constuido con **FastAPI** para la extracción automatizada de titulares y resúmenes de prensa global mediante el agregador Google News (`GNews).

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

Consulta las menciones en prensa de los últimos siete días sobre una entidad.


## ⚡ Ejuctar el servicio

### Pasos

1. **Situarse en el Directorio**: Abre tu terminal y navega hasta el directorio raíz del proyecto.

2. **Construir e iniciar**: Ejecuta el siguiente comando. La instrucción `--build` garantiza que tu imagen se construya con el código más reciente antes de iniciar el contenedor.

```bash
docker compose up --build -d
```

3. **Acceder a la API**: El microservicio estará accesible en el puerto `8082` (definido en el docker-compose.yml). Utiliza tu navegador o una herramienta como cURL o Postman para realizar la siguiente peticion:

| Endpoint | URL Ejemplo |
| :--- | :--- |
| News | `http://127.0.0.1:8082/news/Apple` |
