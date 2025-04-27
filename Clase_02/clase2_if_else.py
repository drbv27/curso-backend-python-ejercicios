# Ejemplo: Par o Impar
numero_str = input("Ingresa un número entero: ")
numero = int(numero_str)

# Si el residuo de dividir entre 2 es 0, es par.
if numero % 2 == 0:
    # Bloque si la condición (numero % 2 == 0) es True
    print(f"El número {numero} es PAR.")
else:
    # Bloque si la condición (numero % 2 == 0) es False
    print(f"El número {numero} es IMPAR.")

print("Análisis de paridad completado.")


# Ejemplo: Mayoría de Edad
edad_usuario_str = input("\nPor favor, introduce tu edad: ")
edad_usuario = int(edad_usuario_str)

if edad_usuario >= 18:
    print("Acceso permitido. Eres mayor de edad.")
else:
    print("Acceso denegado. Eres menor de edad.")

print("Gracias por usar nuestro sistema.")