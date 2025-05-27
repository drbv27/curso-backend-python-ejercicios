# 🌐 Clase 8: Introducción al Desarrollo Web con Flask (Parte 1)

¡Bienvenidos al emocionante mundo del desarrollo web! En esta clase, damos nuestros primeros pasos con Flask, un microframework de Python, para construir aplicaciones web.

## ✅ Temas Cubiertos

- **Fundamentos Web**: Modelo Cliente-Servidor, protocolo HTTP (Peticiones/Respuestas, Métodos GET/POST, Códigos de Estado).
- **Frameworks Web**: Qué son y por qué los usamos. Introducción a Flask como microframework.
- **Instalación y Configuración**:
  - Creación y activación de **Entornos Virtuales (`venv`)**.
  - Instalación de Flask con `pip install Flask`.
  - `requirements.txt` para gestionar dependencias.
- **Aplicación "Hola Mundo" con Flask**:
  - `app = Flask(__name__)`.
  - `app.run(debug=True)`.
- **Rutas (Routing)**:
  - Decorador `@app.route('/ruta')` para mapear URLs a funciones de vista.
  - **Rutas Dinámicas**: Capturar variables de la URL (ej: `@app.route('/usuario/<nombre>')`).
  - **Conversores de Tipo**: `<int:id>`, `<float:precio>`.
- **Métodos HTTP**: Especificar `methods=['GET', 'POST']` (introducción).
- **Objeto `request`**: Acceder a datos de la petición (ej: `request.args.get('parametro')` para query strings).
- **Generación de Respuestas**:
  - Retornar strings y HTML simple.
  - Retornar códigos de estado HTTP (ej: `return "Error", 404`).
- **Plantillas HTML con `render_template()` (Introducción)**:
  - Crear carpeta `templates/`.
  - Sintaxis básica de Jinja2 `{{ variable }}` para pasar datos de Python al HTML.
  - `return render_template('archivo.html', var_py=valor)`.

## 💻 Archivos de Código

- [`app.py`](./app.py): Aplicación Flask principal que contiene todos los ejemplos de rutas (estáticas, dinámicas), manejo básico de `request.args`, y demostraciones de `render_template` desarrollados en clase, incluyendo los ejercicios de práctica.
- `templates/`:
  - [`mi_plantilla.html`](./templates/mi_plantilla.html): Plantilla HTML simple usada para demostrar cómo `render_template` pasa variables a un archivo HTML.
  - [`favoritos.html`](./templates/favoritos.html): Plantilla HTML usada en el ejercicio de práctica para mostrar una lista de ítems usando un bucle Jinja2.

## 🎯 Tareas / Ejercicios Propuestos

1.  **Mini-Sitio Estático Personal:**
    - Crea una aplicación Flask con al menos 3-4 páginas (ej: Inicio, Sobre Mí, Proyectos, Contacto).
    - Cada página debe ser un archivo HTML separado dentro de la carpeta `templates/`.
    - Cada página debe ser servida por una ruta distinta en tu `app.py` usando `render_template()`.
    - Pasa al menos un título de página dinámico a cada plantilla.
    - _(Opcional)_ Crea un archivo `static/style.css` básico y enlázalo en tus plantillas usando `{{ url_for('static', filename='style.css') }}`. (Esto requiere crear una carpeta `static` al mismo nivel que `templates`).
2.  **Calculadora por URL (GET):**
    - Crea una aplicación Flask con una ruta como `/calculadora/<operacion>/<float:num1>/<float:num2>`.
    - El parámetro `operacion` debe ser un string (ej: "sumar", "restar", "multiplicar", "dividir").
    - La función de vista asociada debe tomar estos tres parámetros, realizar la operación matemática correspondiente y retornar el resultado como un string formateado (ej: `"La suma de 10.5 y 3.2 es 13.7"`).
    - Maneja el caso de la división por cero (puedes retornar un mensaje de error y un código de estado `400 Bad Request`).
    - Maneja el caso de una operación no reconocida.

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_08/`._
