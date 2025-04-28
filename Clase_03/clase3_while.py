# archivo: clase3_while.py

print("--- Contando con while ---")
contador = 1  # 1. Inicialización
while contador <= 5: # 2. Condición
    print(f"Contador vale: {contador}")
    contador = contador + 1 # 3. Actualización (¡Importantísimo!)
    # Alternativa más corta: contador += 1
print("Fin del bucle while.")


print("\n--- Sumar números hasta ingresar 0 ---")
suma_total = 0
# Pedimos el primer número ANTES del bucle
numero_str = input("Introduce un número (o 0 para terminar): ")
# Idealmente validar con try-except aquí también
numero = int(numero_str)

while numero != 0: # La condición es que el número NO sea 0
    suma_total += numero # Acumulamos la suma
    # Pedimos el SIGUIENTE número DENTRO del bucle
    numero_str = input("Introduce otro número (o 0 para terminar): ")
    numero = int(numero_str) # Actualizamos la variable de la condición

print(f"La suma total de los números ingresados es: {suma_total}")