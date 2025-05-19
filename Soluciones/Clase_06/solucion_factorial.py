# Solución Tarea Clase 6: Factorial de un Número

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    n! = n * (n-1) * (n-2) * ... * 1
    0! = 1

    Args:
        n (int): Un número entero no negativo.

    Returns:
        int: El factorial de n.
        str: Mensaje de error si n es negativo o no es entero.
    """
    if not isinstance(n, int):
        return "Error: La entrada debe ser un número entero."
    if n < 0:
        return "Error: El factorial no está definido para números negativos."
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1): # Desde 1 hasta n (inclusive)
            resultado *= i
        return resultado

print("--- Calculadora de Factorial ---")
try:
    num = int(input("Introduce un número entero no negativo para calcular su factorial: "))
    resultado_fact = factorial(num)
    if isinstance(resultado_fact, str): # Si la función retornó un mensaje de error
        print(resultado_fact)
    else:
        print(f"El factorial de {num} (es decir, {num}!) es: {resultado_fact}")
except ValueError:
    print("Entrada inválida. Debes introducir un número entero.")

print(f"Prueba con 0!: {factorial(0)}")
print(f"Prueba con 5!: {factorial(5)}")
print(f"Prueba con -3!: {factorial(-3)}")
print(f"Prueba con 3.5!: {factorial(3.5)}")
print("-" * 20)