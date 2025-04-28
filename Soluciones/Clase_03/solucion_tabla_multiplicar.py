# Solución Tarea Clase 3: Tabla de Multiplicar

print("--- Tabla de Multiplicar ---")

num_str = input("Introduce un número entero para ver su tabla de multiplicar: ")

try:
    numero = int(num_str)
    print(f"\nTabla de multiplicar del {numero}:")

    # Usamos for con range(1, 11) para ir del 1 al 10
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Error: Debes introducir un número entero válido.")

print("-" * 20)