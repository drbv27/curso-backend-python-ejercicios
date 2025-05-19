# archivo: clase6_docstrings.py

def calcular_potencia(base, exponente):
    """
    Calcula la potencia de un número.

    Esta función toma una base y un exponente, y devuelve
    el resultado de elevar la base al exponente.

    Args:
        base (int o float): El número base.
        exponente (int o float): El exponente al que se eleva la base.

    Returns:
        int o float: El resultado de base elevado al exponente.
        str: Mensaje de error si la base es negativa y el exponente no es entero,
             o si el cálculo resulta en un número demasiado grande (ejemplo).
    """
    # Ejemplo de validación simple (se pueden añadir más)
    if isinstance(base, (int, float)) and isinstance(exponente, (int, float)):
        if base < 0 and not isinstance(exponente, int):
            return "Error: Base negativa con exponente no entero no está definido aquí."
        try:
            resultado = base ** exponente
            return resultado
        except OverflowError:
            return "Error: Resultado demasiado grande."
    else:
        return "Error: Base y exponente deben ser numéricos."

# Para ver el docstring:
help(calcular_potencia)

print("\nDocstring directamente con __doc__:")
print(calcular_potencia.__doc__)

print(f"\n2 elevado a 3: {calcular_potencia(2,3)}")
print(f"10 elevado a 0.5: {calcular_potencia(10,0.5)}")
print(f"-2 elevado a 2: {calcular_potencia(-2,2)}")
print(f"-2 elevado a 0.5: {calcular_potencia(-2,0.5)}")