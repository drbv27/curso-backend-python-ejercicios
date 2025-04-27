# Ejercicio 1: Mayoría de Edad (Refuerzo)
print("--- Ejercicio 1: Mayoría de Edad ---")
edad_str = input("Introduce tu edad: ")
# Idealmente, deberíamos validar que sea un número, pero lo omitimos por ahora.
edad = int(edad_str)

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
print("-" * 20)


# Ejercicio 2: Calificación de Notas
print("--- Ejercicio 2: Calificación de Notas ---")
nota_str = input("Introduce tu nota (0-100): ")
# Convertimos a float para permitir decimales si el usuario los pone
# Añadimos validación de entrada con try-except (un adelanto!)
try:
    nota = float(nota_str)

    # Primero, validamos si la nota está en el rango permitido
    if nota < 0 or nota > 100:
        calificacion = "Nota inválida (fuera de rango 0-100)"
    # Si la nota es válida, procedemos a clasificarla
    elif nota >= 90:
        calificacion = "Sobresaliente"
    elif nota >= 70:
        calificacion = "Notable"
    elif nota >= 50:
        calificacion = "Aprobado"
    else: # Si llega aquí, sabemos que es >= 0 y < 50
        calificacion = "Suspenso"

    print(f"Calificación: {calificacion}")

except ValueError:
    print("Error: Entrada inválida. Debes introducir un número.")

print("-" * 20)


# Ejercicio 3: Login Simple
print("--- Ejercicio 3: Login Simple ---")
# Credenciales correctas definidas en el código
usuario_correcto = "usuario_test"
password_correcto = "qwertY_1"

# Solicitud de datos al usuario
usuario_ingresado = input("Ingrese su nombre de usuario: ")
password_ingresada = input("Ingrese su contraseña: ")

# Verificación usando 'if' y 'and'
if usuario_ingresado == usuario_correcto and password_ingresada == password_correcto:
    print("¡Acceso concedido!")
else:
    print("Error: Nombre de usuario o contraseña incorrectos.")
print("-" * 20)