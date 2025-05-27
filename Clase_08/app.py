# Clase_08/app.py
from flask import Flask, request, render_template
import datetime

# 1. Creamos una instancia de la aplicación Flask.
app = Flask(__name__) # __name__ es el nombre del módulo actual.

# 2. Ruta Raíz y función de vista básica
@app.route('/')
def hola_mundo():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    # Lo que retorna esta función es lo que se enviará de vuelta al navegador.
    return f"¡Hola, Mundo desde Flask! Son las {hora_actual}."

# --- Rutas Estáticas Adicionales ---
@app.route('/bienvenida')
def pagina_bienvenida():
    return "¡Bienvenido a mi primera aplicación web con Flask!"

@app.route('/info')
def pagina_info():
    return "Esta aplicación está construida con Python y Flask."

@app.route('/contacto')
@app.route('/contactanos') # Múltiples rutas para la misma función
def pagina_contacto():
    return "Puedes contactarnos en: curso.flask@example.com"

# --- Rutas Dinámicas ---
@app.route('/usuario/<nombre>') # <nombre> es la parte variable
def perfil_usuario(nombre):     # El valor capturado se pasa como argumento 'nombre'
    return f"<h1>Perfil de {nombre.capitalize()}</h1><p>Bienvenido a tu espacio, {nombre.capitalize()}.</p>"

@app.route('/post/<int:post_id>') # post_id debe ser un entero
def mostrar_post(post_id):
    return f"Viendo el contenido del post número: {post_id} (Tipo: {type(post_id)})"

@app.route('/precio/<float:valor_precio>') # valor_precio DEBE ser un float
def mostrar_precio(valor_precio):
    return f"El precio es: ${valor_precio:.2f}"

# --- Métodos HTTP y Objeto request (Ejemplo Básico) ---
@app.route('/login_ejemplo', methods=['GET', 'POST'])
def pagina_login_ejemplo():
    if request.method == 'POST':
        # Lógica para procesar datos de login enviados por POST (se verá en detalle después)
        # Por ahora, simulamos recibir un nombre.
        nombre_enviado = request.form.get('nombre_usuario_form', 'Usuario Desconocido')
        return f"Formulario RECIBIDO por POST. Bienvenido, {nombre_enviado}!"
    else: # request.method == 'GET'
        # Lógica para mostrar el formulario de login (o un mensaje)
        return """
            <p>Este es el formulario de login (GET).</p>
            <form method="POST">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre_usuario_form"><br><br>
                <input type="submit" value="Enviar por POST">
            </form>
        """

@app.route('/buscar')
def pagina_buscar():
    termino_busqueda = request.args.get('termino', 'Nada')
    limite = request.args.get('limite', '10', type=int)
    return f"Resultados de búsqueda para: '{termino_busqueda}'. Límite: {limite}."

# --- Respuestas y Renderizado HTML Básico ---
@app.route('/html_directo')
def html_directo():
    return """
        <!DOCTYPE html><html><head><title>HTML Directo</title></head>
        <body><h1>Página Simple</h1><p>Este HTML fue generado como un string.</p>
        <ul><li>Item 1</li><li>Item 2</li></ul></body></html>
    """

@app.route('/recurso_no_encontrado_demo')
def pagina_404_demo():
    return "¡Oops! El recurso que buscas no está aquí.", 404

# Renderizado con render_template
@app.route('/saludo_con_plantilla/<nombre>')
def saludo_con_plantilla(nombre):
    titulo_web = f"Saludo para {nombre}"
    encabezado_web = "Bienvenida Dinámica desde Plantilla"
    mensaje_dinamico = "¡Gracias por visitar nuestra página creada con Flask y Jinja2!"
    sentimiento = "genial"
    return render_template('mi_plantilla.html',
                           titulo_de_pagina=titulo_web,
                           encabezado=encabezado_web,
                           nombre_usuario=nombre,
                           mensaje_adicional=mensaje_dinamico,
                           dia_sentimiento=sentimiento)

# --- Rutas para la Práctica Guiada de Clase ---
@app.route('/practica/') # Añadimos una barra al final para consistencia
def index_practica():
    return "Bienvenido a Mi Aplicación Flask de Práctica"

@app.route('/practica/sobre_mi')
def sobre_mi_practica():
    return "<h2>Un Poco Sobre Mí</h2><p>Soy un entusiasta del desarrollo backend aprendiendo Flask.</p>"

@app.route('/practica/edad_futura/<nombre>/<int:edad_actual>')
def edad_futura_practica(nombre, edad_actual):
    edad_en_5 = edad_actual + 5
    return f"Hola {nombre.capitalize()}, en 5 años tendrás {edad_en_5} años."

@app.route('/practica/mis_datos_favoritos')
def mis_datos_favoritos_practica():
    titulo = "Mis Cosas Favoritas (Práctica)"
    favoritos = ["Aprender Python", "Construir APIs", "El café de la mañana", "Resolver problemas"]
    return render_template('favoritos.html', titulo_pagina=titulo, items_lista=favoritos)


# Este bloque es crucial para ejecutar la aplicación.
if __name__ == '__main__':
    # app.run() inicia el servidor de desarrollo incorporado de Flask.
    # debug=True es muy útil para desarrollo.
    # host='0.0.0.0' hace que el servidor sea accesible desde otras máquinas en la red local.
    app.run(debug=True, host='0.0.0.0')