# Solución Tarea Clase 5: Directorio Telefónico

directorio = {}

def mostrar_menu():
    print("\n--- Directorio Telefónico ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    return input("Elige una opción: ")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nombre = input("Nombre del contacto: ").strip().capitalize()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        telefono = input("Número de teléfono: ").strip()
        if not telefono:
            print("El teléfono no puede estar vacío.")
            continue
        directorio[nombre] = telefono
        print(f"Contacto '{nombre}' añadido/actualizado.")

    elif opcion == "2":
        nombre_buscar = input("Nombre del contacto a buscar: ").strip().capitalize()
        telefono_encontrado = directorio.get(nombre_buscar)
        if telefono_encontrado:
            print(f"Teléfono de {nombre_buscar}: {telefono_encontrado}")
        else:
            print(f"Contacto '{nombre_buscar}' no encontrado.")

    elif opcion == "3":
        nombre_eliminar = input("Nombre del contacto a eliminar: ").strip().capitalize()
        if nombre_eliminar in directorio:
            telefono_eliminado = directorio.pop(nombre_eliminar)
            print(f"Contacto '{nombre_eliminar}' (Tel: {telefono_eliminado}) eliminado.")
        else:
            print(f"Contacto '{nombre_eliminar}' no encontrado para eliminar.")

    elif opcion == "4":
        if not directorio:
            print("El directorio está vacío.")
        else:
            print("\n--- Lista de Contactos ---")
            for nombre, telefono in directorio.items():
                print(f"- {nombre}: {telefono}")
            print("-------------------------")
    elif opcion == "5":
        print("Saliendo del directorio. ¡Adiós!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")