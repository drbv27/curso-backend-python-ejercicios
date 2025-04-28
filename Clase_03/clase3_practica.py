# archivo: clase3_practica.py

# Ejercicio 1: Adivina la Contraseña (while)
print("--- Ejercicio 1: Adivina la contraseña ---")
contraseña_secreta = "secreto123"
intento_usuario = ""

# Continuar mientras el intento NO SEA igual a la secreta
while intento_usuario != contraseña_secreta:
    intento_usuario = input("Introduce la contraseña: ")
    if intento_usuario == contraseña_secreta:
        print("¡Contraseña correcta! Acceso concedido.")
        # El bucle terminará naturalmente porque la condición será False
    else:
        print("Incorrecta. Intenta de nuevo.")
print("-" * 20)


# Ejercicio 2: Suma del 1 al 100 (for)
print("--- Ejercicio 2: Suma del 1 al 100 ---")
suma_acumulada = 0  # Inicializamos el acumulador

# range(1, 101) incluye 1 y va hasta 100
for numero in range(1, 101):
    suma_acumulada += numero # Sumamos el número actual al acumulador

# Imprimimos el resultado DESPUÉS de que el bucle haya terminado
print(f"La suma de los números del 1 al 100 es: {suma_acumulada}")
print("-" * 20)


# Ejercicio 3: Omitir Múltiplos de 3 (for/if/continue)
print("--- Ejercicio 3: Imprimir 1-20 omitiendo múltiplos de 3 ---")
for numero in range(1, 21): # Del 1 al 20
    # Comprobamos si es múltiplo de 3
    if numero % 3 == 0:
        # Si es múltiplo, saltamos al siguiente número sin imprimir
        continue
    # Si no es múltiplo de 3, sí lo imprimimos
    print(numero, end=" ") # end=" " para imprimir en la misma línea

print() # Imprime un salto de línea final
print("-" * 20)