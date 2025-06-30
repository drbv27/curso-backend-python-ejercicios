# Soluciones/Clase_09/solucion_formulario_contacto/app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
import os

app = Flask(__name__)
app.secret_key = "mi_clave_super_secreta_para_contacto"
CONTACTOS_FILE = "mensajes_contacto.txt"

@app.route('/', methods=['GET', 'POST'])
def formulario_contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')

        if not nombre or not email or not mensaje:
            flash("Todos los campos son obligatorios.", "error")
        elif not nombre.strip() or not email.strip() or not mensaje.strip():
            flash("Los campos no pueden consistir solo de espacios.", "error")
        else:
            # Guardar en archivo
            try:
                ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                linea_contacto = f"Fecha: {ahora}\nNombre: {nombre}\nEmail: {email}\nMensaje:\n{mensaje}\n{'-'*30}\n"
                with open(CONTACTOS_FILE, "a") as f:
                    f.write(linea_contacto)
                flash("¡Mensaje enviado con éxito! Gracias por contactarnos.", "success")
                return redirect(url_for('formulario_contacto')) # Redirige para limpiar formulario
            except IOError:
                flash("Hubo un error al guardar tu mensaje. Inténtalo más tarde.", "error")

    # Para GET o después de la redirección
    return render_template('contacto_form.html', titulo_pagina="Formulario de Contacto")


@app.route('/ver_mensajes') # Ruta opcional para ver los mensajes guardados
def ver_mensajes():
    mensajes_guardados = ""
    if os.path.exists(CONTACTOS_FILE):
        try:
            with open(CONTACTOS_FILE, "r") as f:
                mensajes_guardados = f.read()
        except IOError:
            mensajes_guardados = "Error al leer los mensajes."
    else:
        mensajes_guardados = "Aún no hay mensajes."
    # Usaremos una plantilla simple para mostrarlo
    return render_template('ver_mensajes_contacto.html', mensajes=mensajes_guardados, titulo_pagina="Mensajes Recibidos")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)