# Soluciones/Clase_08/solucion_mini_sitio_estatico/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html', titulo="Página de Inicio")

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('acerca.html', titulo="Quiénes Somos")

@app.route('/servicios')
def servicios():
    lista_servicios = [
        "Desarrollo Web con Python y Flask",
        "Creación de APIs RESTful",
        "Consultoría Tecnológica"
    ]
    return render_template('servicios.html', titulo="Nuestros Servicios", servicios=lista_servicios)

@app.route('/contacto')
def contacto():
    info_contacto = {
        "email": "contacto@misitioflask.com",
        "telefono": "+57 123 4567890",
        "ciudad": "Medellín, Colombia"
    }
    return render_template('contacto.html', titulo="Página de Contacto", contacto=info_contacto)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')