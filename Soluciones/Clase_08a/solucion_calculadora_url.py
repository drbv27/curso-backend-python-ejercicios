# Soluciones/Clase_08/solucion_calculadora_url.py
from flask import Flask

app = Flask(__name__)

@app.route('/calculadora/<string:operacion>/<float:num1>/<float:num2>')
def calculadora_url(operacion, num1, num2):
    resultado = None
    error = None

    if operacion == "sumar":
        resultado = num1 + num2
    elif operacion == "restar":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        if num2 == 0:
            error = "Error: No se puede dividir por cero."
            return error, 400 # Bad Request
        else:
            resultado = num1 / num2
    else:
        error = f"Error: Operación '{operacion}' no reconocida. Use 'sumar', 'restar', 'multiplicar' o 'dividir'."
        return error, 400 # Bad Request

    if resultado is not None:
        return f"El resultado de {operacion} {num1} y {num2} es: {resultado:.2f}"
    else: # Debería haber sido manejado por los returns de error, pero por si acaso.
         return "Error desconocido en la operación.", 500


@app.route('/')
def index():
    return """
    <h1>Calculadora por URL</h1>
    <p>Ejemplos de uso:</p>
    <ul>
        <li><a href="/calculadora/sumar/10/5">/calculadora/sumar/10/5</a></li>
        <li><a href="/calculadora/restar/100.5/50.2">/calculadora/restar/100.5/50.2</a></li>
        <li><a href="/calculadora/multiplicar/7/6">/calculadora/multiplicar/7/6</a></li>
        <li><a href="/calculadora/dividir/20/4">/calculadora/dividir/20/4</a></li>
        <li><a href="/calculadora/dividir/10/0">/calculadora/dividir/10/0 (Error)</a></li>
        <li><a href="/calculadora/potencia/2/3">/calculadora/potencia/2/3 (Error de operación)</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')