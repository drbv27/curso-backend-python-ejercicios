# Solución Tarea Clase 1: Conversor Celsius a Fahrenheit

print("--- Conversor de Celsius a Fahrenheit ---")

celsius_str = input("Introduce la temperatura en grados Celsius: ")

try:
    # Intentamos convertir la entrada a un número flotante
    celsius = float(celsius_str)

    # Aplicamos la fórmula de conversión
    fahrenheit = (celsius * 9/5) + 32

    # Mostramos el resultado formateado
    # Usamos :.2f para mostrar el resultado Fahrenheit con 2 decimales
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

except ValueError:
    # Si la conversión a float falla (el usuario no introdujo un número)
    print("Error: Entrada inválida. Debes introducir un valor numérico para los grados Celsius.")

print("-" * 20)