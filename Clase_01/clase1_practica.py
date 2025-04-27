# Ejercicio 1: Saludo Personalizado (Versión con Año de Nacimiento)
print("--- Ejercicio 1: Saludo Personalizado ---")

# Pedimos los datos al usuario
nombre_usuario = input("¿Cuál es tu nombre? ")
año_nacimiento_str = input("¿En qué año naciste? ")

# Convertimos el año de nacimiento a entero
año_nacimiento = int(año_nacimiento_str)

# Obtenemos el año actual (forma simple para el ejercicio)
año_actual = 2025 # ¡Asegúrate de usar el año correcto!
# Forma avanzada:
# import datetime
# año_actual = datetime.datetime.now().year

# Calculamos la edad
edad_aproximada = año_actual - año_nacimiento

# Mostramos el saludo usando f-string
print(f"¡Hola {nombre_usuario}! Si naciste en {año_nacimiento}, tienes o cumplirás {edad_aproximada} años en {año_actual}.")
print("-" * 20)


# Ejercicio 2: Calculadora de Rectángulo
print("--- Ejercicio 2: Calculadora de Rectángulo ---")

# Pedimos los datos (usaremos float para permitir decimales)
base_str = input("Introduce la longitud de la base del rectángulo: ")
altura_str = input("Introduce la altura del rectángulo: ")

# Convertimos a float
base = float(base_str)
altura = float(altura_str)

# Calculamos área y perímetro
area = base * altura
perimetro = 2 * (base + altura) # Usando paréntesis

# Mostramos los resultados
print(f"Un rectángulo con base {base} y altura {altura}:")
print(f"- Tiene un área de: {area}")
print(f"- Tiene un perímetro de: {perimetro}")
print("-" * 20)