# Soluciones/Clase_09/solucion_lista_tareas_avanzada/app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import json # Para guardar/cargar tareas en un archivo
import os   # Para verificar si el archivo existe

app = Flask(__name__)
app.secret_key = "clave_secreta_para_tareas_avanzadas_123"

TAREAS_ARCHIVO = "tareas_db.json" # Nombre del archivo para persistencia

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    if not os.path.exists(TAREAS_ARCHIVO):
        return [] # Si no existe el archivo, retorna lista vacía
    try:
        with open(TAREAS_ARCHIVO, "r") as f:
            tareas = json.load(f)
            # Asegurar que cada tarea sea un diccionario con 'texto' y 'completada'
            return [t for t in tareas if isinstance(t, dict) and "texto" in t and "completada" in t]
    except (json.JSONDecodeError, IOError):
        return [] # Si hay error al leer o el JSON está malformado

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    try:
        with open(TAREAS_ARCHIVO, "w") as f:
            json.dump(tareas, f, indent=4)
        return True
    except IOError:
        return False

@app.route('/')
def index_tareas():
    tareas = cargar_tareas()
    return render_template('lista_tareas_avanzada.html', tareas=tareas, titulo_pagina="Mi Lista de Tareas Avanzada")

@app.route('/agregar_tarea_avanzada', methods=['POST'])
def agregar_tarea_avanzada():
    tareas = cargar_tareas()
    descripcion_nueva_tarea = request.form.get('descripcion_tarea')
    if descripcion_nueva_tarea and descripcion_nueva_tarea.strip():
        tareas.append({"texto": descripcion_nueva_tarea.strip(), "completada": False, "id": len(tareas) + 1})
        if guardar_tareas(tareas):
            flash(f"Tarea '{descripcion_nueva_tarea}' añadida con éxito.", "success")
        else:
            flash("Error al guardar la tarea en el archivo.", "error")
    else:
        flash("La descripción de la tarea no puede estar vacía.", "warning")
    return redirect(url_for('index_tareas'))

@app.route('/marcar_completada/<int:tarea_id>', methods=['POST'])
def marcar_completada(tarea_id):
    tareas = cargar_tareas()
    actualizada = False
    for tarea in tareas:
        # Asumimos que los IDs son únicos y se basan en la posición + 1 o un ID real
        # Para un sistema real, los IDs deberían ser más robustos (ej. UUID)
        if tarea.get("id") == tarea_id : # Buscamos por 'id' si lo tiene
            tarea["completada"] = not tarea["completada"] # Toggle completada
            actualizada = True
            break

    if actualizada and guardar_tareas(tareas):
        flash(f"Estado de la tarea ID {tarea_id} actualizado.", "info")
    elif not actualizada:
         flash(f"Tarea con ID {tarea_id} no encontrada.", "error")
    else:
        flash("Error al guardar el estado de la tarea.", "error")
    return redirect(url_for('index_tareas'))

@app.route('/eliminar_tarea/<int:tarea_id>', methods=['POST'])
def eliminar_tarea(tarea_id):
    tareas_originales = cargar_tareas()
    # Filtramos la lista para excluir la tarea con el ID a eliminar
    tareas_actualizadas = [t for t in tareas_originales if t.get("id") != tarea_id]

    if len(tareas_actualizadas) < len(tareas_originales): # Si se eliminó algo
        if guardar_tareas(tareas_actualizadas):
            flash(f"Tarea ID {tarea_id} eliminada.", "success")
        else:
            flash("Error al guardar las tareas después de eliminar.", "error")
    else:
        flash(f"Tarea con ID {tarea_id} no encontrada para eliminar.", "warning")
    return redirect(url_for('index_tareas'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) # Usar puerto diferente si la otra app sigue corriendo