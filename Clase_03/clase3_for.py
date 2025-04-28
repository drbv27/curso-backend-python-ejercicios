# archivo: clase3_for.py

print("--- Iterando sobre un string ---")
nombre = "PYTHON"
for caracter in nombre:
    print(f"Letra actual: {caracter}")


print("\n--- range(stop) ---")
for i in range(5): # Genera 0, 1, 2, 3, 4
    print(f"Iteración número: {i}")


print("\n--- range(start, stop) ---")
for i in range(3, 7): # Genera 3, 4, 5, 6
    print(f"Valor: {i}")


print("\n--- range(start, stop, step) ---")
# Números impares del 1 al 10
print("Impares 1-10:")
for i in range(1, 11, 2): # Genera 1, 3, 5, 7, 9
    print(i, end=" ")
print() # Salto de línea

# Contar hacia atrás
print("\nCuenta regresiva:")
for i in range(5, 0, -1): # Genera 5, 4, 3, 2, 1
    print(i)
print("¡Despegue!")


print("\n--- Identificando pares/impares con for e if ---")
for numero in range(1, 11): # Rango de 1 a 10
    if numero % 2 == 0:
        # Condición dentro del bucle
        print(f"{numero} es PAR")
    else:
        print(f"{numero} es IMPAR")