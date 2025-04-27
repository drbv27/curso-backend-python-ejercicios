# Solución Tarea Clase 2: Feedback de Login Mejorado

print("--- Login Mejorado ---")
# Credenciales correctas
usuario_correcto = "admin_curso"
password_correcto = "Python_R0cks!"

# Solicitud de datos
usuario_ingresado = input("Usuario: ")
password_ingresada = input("Contraseña: ")

# Verificación con feedback específico
if usuario_ingresado == usuario_correcto:
    # El usuario es correcto, ahora verificamos la contraseña
    if password_ingresada == password_correcto:
        print("¡Acceso concedido!")
    else:
        print("Error: Contraseña incorrecta.")
else:
    # El usuario es incorrecto (no hace falta verificar contraseña)
    print("Error: Usuario no encontrado.")

print("-" * 20)