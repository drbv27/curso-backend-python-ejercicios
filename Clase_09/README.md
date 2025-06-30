# 🌐 Clase 9: Fundamentos Web y Protocolo HTTP

En esta clase teórica pero fundamental, desmitificamos cómo funciona la comunicación en internet, sentando las bases para todo el desarrollo web backend.

## ✅ Temas Cubiertos

- **Modelo Cliente-Servidor:** El ciclo de Petición/Respuesta que impulsa la web.
- **Anatomía de una URL:** Desglose de `protocolo://dominio:puerto/ruta?parametros#fragmento`.
- **Protocolo HTTP:**
  - Estructura de Peticiones y Respuestas (Línea de Inicio, Cabeceras, Cuerpo).
  - **Métodos HTTP:** `GET` (pedir), `POST` (enviar/crear), `PUT` (reemplazar), `PATCH` (modificar), `DELETE` (eliminar).
  - **Códigos de Estado HTTP:** Entender `2xx` (Éxito), `3xx` (Redirección), `4xx` (Error del Cliente - ej. `404 Not Found`), `5xx` (Error del Servidor - ej. `500 Internal Server Error`).
- **Formato de Datos JSON:** El estándar para el intercambio de datos en APIs modernas.
- **Herramientas Prácticas:**
  - **Herramientas de Desarrollador del Navegador:** Uso de la pestaña "Network" para inspeccionar tráfico HTTP en vivo.
  - **Librería `requests` de Python:** Para actuar como un cliente HTTP y consumir APIs desde nuestros scripts.

## 🧰 Guía Rápida de Conceptos

| Concepto                        | Descripción                                                                           |
| :------------------------------ | :------------------------------------------------------------------------------------ |
| **`GET`**                       | Pide datos de un servidor. Los parámetros van en la URL. Es seguro e idempotente.     |
| **`POST`**                      | Envía datos a un servidor para crear un recurso. Los datos van en el cuerpo.          |
| **`200 OK`**                    | La petición fue exitosa.                                                              |
| **`404 Not Found`**             | El recurso solicitado no existe en el servidor.                                       |
| **`500 Internal Server Error`** | Algo salió mal en el código del servidor.                                             |
| **JSON**                        | Formato de texto para intercambiar datos, basado en pares clave-valor y listas.       |
| **`requests.get(url)`**         | Función de la librería `requests` para realizar una petición GET.                     |
| **`response.json()`**           | Método del objeto respuesta para decodificar un cuerpo JSON a un dict/list de Python. |

## 💻 Archivos de Código

- [`clase9_practica_requests.py`](./clase9_practica_requests.py): Script de práctica que utiliza la librería `requests` para hacer una petición GET a una API pública (`jsonplaceholder`), inspeccionar la respuesta (código de estado, cabeceras) y procesar los datos JSON recibidos. Incluye manejo de errores básico.

## 🎯 Tareas / Ejercicios Propuestos

1.  **Explorador de APIs Públicas:**
    - Visita el repositorio [public-apis en GitHub](https://github.com/public-apis/public-apis).
    - Elige una API gratuita que no requiera autenticación de una categoría que te interese (ej: `Cat Facts`, `PokéAPI`, `Open Trivia DB`).
    - Crea un script en Python que use la librería `requests` para hacer una petición a uno de sus endpoints.
    - Imprime los datos que recibes de forma organizada y legible. ¡Usa `try-except`!
2.  **Inspección de Sitios Web:**
    - Abre las Herramientas de Desarrollador de tu navegador en la pestaña "Network".
    - Visita 3 de tus sitios web favoritos.
    - Analiza las peticiones que se hacen al cargar la página. ¿Cuál es la petición principal del documento? ¿Qué código de estado tiene? ¿Qué otros recursos (CSS, imágenes, JS) se cargan?
    - Interactúa con los sitios (ej: haz una búsqueda, aplica un filtro). Observa las nuevas peticiones que se generan (a menudo son de tipo `Fetch/XHR`). ¿Puedes ver los datos JSON que se intercambian?

---

_Puedes encontrar una posible solución al ejercicio 1 (usando la PokéAPI) en la carpeta `Soluciones/Clase_09/`._
