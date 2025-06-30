# 🚀 Clase 9: Desarrollo Web con Flask (Parte 2) - Plantillas Avanzadas y Formularios

En esta clase, profundizamos en Flask para construir aplicaciones web más dinámicas e interactivas, dominando el motor de plantillas Jinja2 y el manejo de formularios HTML.

## ✅ Temas Cubiertos

- **Jinja2 Templating Avanzado**:
  - Estructuras de Control: `{% for item in lista %}` (con `loop` y `{% else %}`), `{% if condicion %}` (con `elif`, `else`).
  - Filtros Comunes: `capitalize`, `upper`, `lower`, `length`, `default()`, `round()`, `truncate()`, `safe` (con precaución).
  - **Herencia de Plantillas**:
    - Creación de `base.html` con estructura común.
    - Uso de `{% block nombre_bloque %}` y `{% endblock %}`.
    - Plantillas hijas con `{% extends "base.html" %}`.
- **Navegación y Recursos Estáticos**:
  - Generación dinámica de URLs con `url_for('nombre_funcion_vista', param=valor)`.
  - Servir archivos estáticos (CSS, JS, imágenes) desde la carpeta `static/` usando `url_for('static', filename='ruta/archivo.css')`.
- **Formularios HTML**:
  - Estructura `<form method="..." action="...">` y campos `<input name="...">`.
  - Manejo de peticiones **`GET`**: Datos en la URL, acceso con `request.args.get()`.
  - Manejo de peticiones **`POST`**: Datos en el cuerpo de la petición, acceso con `request.form.get()`. Ruta con `methods=['POST']`.
- **Mejorando la Experiencia del Usuario**:
  - **Patrón Post/Redirect/Get (PRG)** para evitar reenvío de formularios.
  - Redirecciones con `redirect(url_for('otra_vista'))`.
  - **Mensajes Flash**: Notificaciones temporales. Configurar `app.secret_key`. Usar `flash('mensaje', 'categoria')`. Mostrar en plantillas con `get_flashed_messages(with_categories=true)`.

## 💻 Archivos de Código (En esta carpeta `Clase_09/`)

- [`app_clase9.py`](./app_clase9.py): Aplicación Flask principal que integra los ejemplos de Jinja2 avanzado, herencia, `url_for`, estáticos, formularios GET/POST, redirecciones, mensajes flash, y la aplicación de "Lista de Tareas" en memoria desarrollada en la práctica.
- `templates/`:
  - [`base.html`](./templates/base.html): Plantilla base con bloques redefinibles, enlace a CSS y código para mostrar mensajes flash.
  - [`tareas.html`](./templates/tareas.html): Plantilla para la aplicación de lista de tareas, hereda de `base.html`. Muestra tareas y formulario de adición.
  - [`jinja_demo.html`](./templates/jinja_demo.html): Plantilla para demostrar estructuras de control y filtros de Jinja2.
  - [`perfil_simple.html`](./templates/perfil_simple.html): Plantilla simple para demostrar `url_for` con parámetros.
- `static/css/`:
  - [`style.css`](./static/css/style.css): Hoja de estilos básica para `base.html` y los mensajes flash.

## 🎯 Tareas / Ejercicios Propuestos

1.  **Expandir la App de "Lista de Tareas":**
    - Modifica la aplicación de lista de tareas para que los datos **persistan** si reinicias el servidor. Guarda las tareas en un archivo de texto simple o, preferiblemente, en un archivo **JSON** (usando el módulo `json` de Python para `json.dump()` y `json.load()`).
    - Añade la funcionalidad de marcar tareas como "completadas" (podrías añadir un campo booleano `completada` al diccionario de cada tarea). Muestra visualmente si una tarea está completada (ej: tachándola).
    - Añade un botón/enlace para eliminar tareas individuales de la lista (y del archivo).
2.  **Formulario de Contacto Simple:**
    - Crea una nueva aplicación Flask con un formulario de contacto que pida: Nombre, Correo Electrónico y Mensaje.
    - Al enviar el formulario (POST), valida que los campos no estén vacíos.
    - Guarda los datos recibidos en un archivo de texto (`mensajes_contacto.txt`), cada envío en una nueva línea o con algún separador.
    - Muestra un mensaje flash de "¡Mensaje enviado, gracias por contactarnos!" y redirige al mismo formulario (limpio).

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_09/`._
