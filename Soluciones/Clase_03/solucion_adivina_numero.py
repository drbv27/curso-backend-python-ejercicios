# Solución Tarea Clase 3: Juego Adivina el Número

import random # Necesitamos importar el módulo random

print("--- Juego: Adivina el Número ---")
print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

# Generamos el número secreto
numero_secreto = random.randint(1, 100)
intentos = 0 # Contador de intentos
adivinado = False # Bandera para saber si ha adivinado

# Bucle while que continúa mientras no se haya adivinado
while not adivinado:
    intento_str = input("Introduce tu número: ")
    try:
        intento_usuario = int(intento_str)
        intentos += 1 # Incrementamos el contador de intentos

        # Comparamos el intento con el número secreto
        if intento_usuario == numero_secreto:
            print(f"¡Felicidades! ¡Has adivinado el número {numero_secreto} en {intentos} intentos!")
            adivinado = True # Cambiamos la bandera para salir del bucle
            # Alternativamente, podríamos usar 'break' aquí
        elif intento_usuario < numero_secreto:
            print("Demasiado bajo. El número secreto es mayor.")
        else: # Si no es igual ni menor, tiene que ser mayor
            print("Demasiado alto. El número secreto es menor.")

    except ValueError:
        print("Error: Debes introducir un número entero.")

print("-" * 20)