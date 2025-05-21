# archivo: clase7_errores.py

print("--- Manejo de Errores con try-except ---")
try:
    numerador = 10
    denominador_str = input("Introduce un denominador (intenta con 0 o texto): ")
    denominador = int(denominador_str) # Puede dar ValueError
    resultado = numerador / denominador    # Puede dar ZeroDivisionError
    print(f"El resultado de {numerador}/{denominador} es: {resultado}")
except ValueError:
    print("Error: ¡Debes introducir un número entero válido para el denominador!")
except ZeroDivisionError:
    print("Error: ¡No se puede dividir por cero!")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    print(f"Tipo de error: {type(e)}")
print("El programa continúa después del try-except.")
print("-" * 20)


print("--- try-except-else ---")
try:
    edad_str = input("Ingresa tu edad: ")
    edad = int(edad_str)
except ValueError:
    print("Entrada inválida, no es un número.")
else:
    # Esto solo se ejecuta si la conversión a int fue exitosa
    print(f"Tu edad es {edad}. El próximo año tendrás {edad + 1}.")
print("-" * 20)


print("--- try-except-else-finally ---")
try:
    x = 10
    y_str = input("Introduce divisor para 10: ")
    y = int(y_str)
    print(f"Resultado: {x/y}")
except ValueError:
    print("Error: Ingresa un número para el divisor.")
except ZeroDivisionError:
    print("Error: El divisor no puede ser cero.")
except Exception as e: # Captura genérica
    print(f"Error genérico: {e}")
else:
    print("División realizada con éxito.")
finally:
    print("El bloque 'finally' siempre se ejecuta. ¡Limpieza aquí!")
print("-" * 20)