# Clase_09/app_clase9.py
from flask import Flask, render_template, request, redirect, url_for, flash
import datetime

app = Flask(__name__)
# ¡IMPORTANTE! Cambia esto por una clave secreta REAL y aleatoria en una app de producción.
# Puedes generarla con: import os; os.urandom(24)
app.secret_key = "mi_super_clave_secreta_12345_xyz"

# "Base de datos" en memoria para la lista de tareas
# Cada tarea será un diccionario: {"texto": "Descripción", "completada": False}
tareas_pendientes = []

# --- Rutas de Ejemplo Jinja2 y Estáticos ---
@app.route('/jinja_demo')
def jinja_demo():
    usuario_logueado = {"nombre": "Ana", "es_admin": True}
    # usuario_logueado = None
    productos_demo = [
        {"nombre": "Teclado Mecánico", "precio": 75.99, "stock": 10},
        {"nombre": "Mouse Gamer", "precio": 40.50, "stock": 3},
        {"nombre": "Monitor 24 pulgadas", "precio": 180.00, "stock": 7}
    ]
    texto_largo_ejemplo = "Este es un texto bastante largo que usaremos para probar el filtro truncate de Jinja2."
    return render_template('jinja_demo.html', 
                           usuario=usuario_logueado, 
                           productos=productos_demo,
                           texto_largo=texto_largo_ejemplo,
                           titulo_pagina="Demo de Jinja2")

# --- Rutas para la App de Lista de Tareas (Práctica Guiada) ---
@app.route('/')
def mostrar_tareas():
    # Pasamos el año actual para el footer en base.html (ejemplo)
    anio_actual = datetime.datetime.now().year
    return render_template('tareas.html', 
                           tareas=tareas_pendientes, 
                           titulo_pagina="Mi Lista de Tareas",
                           anio_actual=anio_actual)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    descripcion_tarea = request.form.get('descripcion_tarea')
    if descripcion_tarea and descripcion_tarea.strip():
        tareas_pendientes.append({"texto": descripcion_tarea, "completada": False})
        flash(f"Tarea '{descripcion_tarea}' añadida con éxito.", "success")
    else:
        flash("La descripción de la tarea no puede estar vacía.", "error")
    return redirect(url_for('mostrar_tareas'))

@app.route('/limpiar', methods=['POST']) # Usar POST para acciones que modifican datos
def limpiar_tareas():
    # Hacemos global tareas_pendientes para poder reasignarla (borrarla)
    # Aunque para listas, append/pop modifican in-place y no necesitarían global
    # pero reasignar a [] sí lo necesita si está definida fuera.
    # Alternativa: tareas_pendientes.clear() (modifica in-place, no necesita global)
    global tareas_pendientes 
    tareas_pendientes = []
    flash("Todas las tareas han sido eliminadas.", "info")
    return redirect(url_for('mostrar_tareas'))

# --- Ejemplo de ruta para url_for() con parámetros ---
@app.route('/ver_perfil/<username>')
def ver_perfil(username):
    # En una app real, buscarías el usuario y mostrarías su perfil
    return render_template('perfil_simple.html', nombre_usuario=username, titulo_pagina=f"Perfil de {username}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')