# Soluciones/Clase_07/solucion_gestor_notas_simple.py

# Primero, creamos el módulo de utilidades para notas
# Idealmente, este sería un archivo separado: `modulo_notas_util.py`
# --- Contenido de modulo_notas_util.py ---
# import datetime
#
# NOMBRE_ARCHIVO_NOTAS = "notas_persistentes.txt"
#
# def anadir_nota(texto_nota):
#     """Añade una nota al archivo con fecha y hora."""
#     if not texto_nota.strip():
#         return "Error: La nota no puede estar vacía."
#     try:
#         ahora = datetime.datetime.now()
#         fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
#         with open(NOMBRE_ARCHIVO_NOTAS, "a") as f:
#             f.write(f"[{fecha_hora}] {texto_nota}\n")
#         return "Nota añadida con éxito."
#     except IOError as e:
#         return f"Error al escribir en el archivo: {e}"
#
# def ver_notas():
#     """Lee y devuelve todas las notas del archivo."""
#     try:
#         with open(NOMBRE_ARCHIVO_NOTAS, "r") as f:
#             contenido = f.read()
#             if not contenido.strip():
#                 return "(No hay notas guardadas)."
#             return contenido
#     except FileNotFoundError:
#         return "(Archivo de notas no encontrado. Añade una nota para crearlo)."
#     except IOError as e:
#         return f"Error al leer el archivo: {e}"
#
# if __name__ == "__main__":
#     # Pequeñas pruebas del módulo
#     print(anadir_nota("Comprar leche para el desayuno."))
#     print("\n--- Viendo notas desde el módulo ---")
#     print(ver_notas())
# --- Fin de modulo_notas_util.py ---


# --- Script Principal (solucion_gestor_notas_simple.py) ---
# Asumimos que modulo_notas_util.py está en la misma carpeta
# o en una ruta accesible por Python.
# Para este ejemplo, simularemos que está aquí para simplicidad.

import datetime # Necesario para la versión integrada

NOMBRE_ARCHIVO_NOTAS = "notas_persistentes_gestor.txt"

def anadir_nota_gestor(texto_nota):
    """Añade una nota al archivo con fecha y hora."""
    if not texto_nota.strip():
        print("Error: La nota no puede estar vacía.")
        return
    try:
        ahora = datetime.datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
        with open(NOMBRE_ARCHIVO_NOTAS, "a") as f:
            f.write(f"[{fecha_hora}] {texto_nota}\n")
        print("Nota añadida con éxito.")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

def ver_notas_gestor():
    """Lee y muestra todas las notas del archivo."""
    try:
        with open(NOMBRE_ARCHIVO_NOTAS, "r") as f:
            print("\n--- Notas Guardadas ---")
            contenido = f.read()
            if not contenido.strip():
                print("(No hay notas guardadas).")
            else:
                print(contenido.strip())
            print("----------------------")
    except FileNotFoundError:
        print("(Archivo de notas no encontrado. Añade una nota para crearlo).")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

def menu_principal():
    print("\n--- Gestor de Notas Simple ---")
    print("1. Añadir nueva nota")
    print("2. Ver todas las notas")
    print("3. Salir")
    return input("Elige una opción: ")

if __name__ == "__main__":
    while True:
        opcion = menu_principal()
        if opcion == "1":
            nota_usuario = input("Escribe tu nota: ")
            anadir_nota_gestor(nota_usuario)
        elif opcion == "2":
            ver_notas_gestor()
        elif opcion == "3":
            print("Saliendo del gestor de notas.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")