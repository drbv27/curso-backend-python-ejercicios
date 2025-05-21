# archivo: mis_operaciones.py
"""Este es nuestro primer módulo con operaciones básicas."""

PI = 3.14159 # Una variable/constante en el módulo

def sumar(a, b):
    """Retorna la suma de a y b."""
    return a + b

def restar(a, b):
    """Retorna la resta de b a a."""
    return a - b

def saludar_modulo():
    print("¡Hola desde el módulo mis_operaciones!")

def una_funcion_mas():
    return "Esta es otra función útil"

# Código de prueba o demostración
if __name__ == "__main__":
    print("--- Ejecutando mis_operaciones.py como script principal ---")
    print("Probando la función sumar(1,1):", sumar(1,1))
    print("Probando la función restar(5,2):", restar(5,2))
    print(una_funcion_mas())
    print("--- Fin de las pruebas del módulo mis_operaciones ---")