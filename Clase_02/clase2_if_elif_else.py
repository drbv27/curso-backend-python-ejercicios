# Ejemplo: Clasificar un número
numero_str = input("Introduce un número cualquiera: ")
numero = float(numero_str) # Usamos float por si ponen decimales

print("Clasificando el número...")

if numero > 0:
    # Se ejecuta solo si numero > 0 es True
    print("El número es POSITIVO.")
elif numero < 0:
    # Se ejecuta solo si numero > 0 es False Y numero < 0 es True
    print("El número es NEGATIVO.")
else:
    # Se ejecuta solo si las dos condiciones anteriores son False
    print("El número es CERO.")

print("Análisis del número terminado.")


# Ejemplo: Saludo según la hora
hora_str = input("\nIntroduce la hora (formato 0-23): ")
hora = int(hora_str)

print("Evaluando saludo...")

if hora < 0 or hora > 23:
    print("Hora inválida.")
elif hora < 12: # Si llega aquí, sabemos que hora >= 0
    print("¡Buenos días!")
elif hora < 18: # Si llega aquí, sabemos que hora >= 12
    print("¡Buenas tardes!")
else: # Si llega aquí, sabemos que hora >= 18 y <= 23
    print("¡Buenas noches!")

print("¡Que tengas un excelente día!")