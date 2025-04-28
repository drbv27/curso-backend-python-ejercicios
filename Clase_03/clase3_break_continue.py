# archivo: clase3_break_continue.py

print("--- Sumar positivos (0 o negativo para salir con break) ---")
suma_positivos = 0
while True: # Empezamos un bucle potencialmente infinito
    numero_str = input("Introduce un número POSITIVO (0 o negativo para salir): ")
    try:
        numero = int(numero_str)

        if numero <= 0: # Condición de salida
            print("Número no positivo ingresado. Terminando suma.")
            break # ¡Salimos del bucle while inmediatamente!

        # Si llegamos aquí, el número es positivo, lo sumamos
        suma_positivos += numero
        print(f"(Suma parcial: {suma_positivos})")
    except ValueError:
        print("Error: Ingresa un número válido.")

print(f"La suma total de números positivos es: {suma_positivos}")


print("\n--- Imprimir 1-7 saltando 3 y 5 con continue ---")
num = 0
while num < 7:
    num += 1 # Incrementamos primero

    if num == 3 or num == 5:
        print(f"(Saltando el {num})")
        continue # Vuelve al 'while num < 7' sin ejecutar el print de abajo

    # Este print solo se ejecuta si no se hizo 'continue'
    print(f"Número procesado: {num}")

print("Fin del bucle con continue.")