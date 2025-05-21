# Soluciones/Clase_07/solucion_explorar_os_json.py
import os
import json
import datetime

print("--- Explorando el Módulo OS ---")

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar archivos y directorios en el directorio actual
print("\nContenido del directorio actual:")
try:
    for item in os.listdir(directorio_actual):
        print(f"- {item}")
except OSError as e:
    print(f"Error listando directorio: {e}")

# Crear un nombre de archivo uniéndolo al directorio actual
nombre_archivo_test = "test_os_json.txt"
ruta_completa = os.path.join(directorio_actual, nombre_archivo_test)
print(f"\nRuta completa para test: {ruta_completa}")

# Verificar si un archivo existe
if os.path.exists(ruta_completa):
    print(f"El archivo '{nombre_archivo_test}' ya existe.")
    # Podríamos eliminarlo para la prueba:
    # try:
    #     os.remove(ruta_completa)
    #     print(f"Archivo '{nombre_archivo_test}' eliminado para la prueba.")
    # except OSError as e:
    #     print(f"Error eliminando archivo: {e}")
else:
    print(f"El archivo '{nombre_archivo_test}' no existe (se creará).")

print("-" * 20)


print("\n--- Explorando el Módulo JSON ---")
# Datos de ejemplo (lista de diccionarios)
usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True},
    {"id": 2, "nombre": "Luis", "email": "luis@example.com", "activo": False},
    {"id": 3, "nombre": "Eva", "email": "eva@example.com", "activo": True, "ultima_conexion": str(datetime.date.today())}
]
nombre_archivo_json = "usuarios.json"

# Guardar datos en un archivo JSON (serializar)
print(f"\nGuardando datos en '{nombre_archivo_json}'...")
try:
    with open(nombre_archivo_json, "w") as f_json_out:
        json.dump(usuarios, f_json_out, indent=4) # indent=4 para formato legible
    print("Datos guardados en JSON con éxito.")
except IOError as e:
    print(f"Error al escribir archivo JSON: {e}")
except TypeError as e:
    print(f"Error de tipo al serializar a JSON (¿objetos no serializables?): {e}")


# Leer datos de un archivo JSON (deserializar)
print(f"\nLeyendo datos de '{nombre_archivo_json}'...")
try:
    with open(nombre_archivo_json, "r") as f_json_in:
        datos_leidos = json.load(f_json_in)
    print("Datos leídos de JSON con éxito:")
    if isinstance(datos_leidos, list):
        for usuario in datos_leidos:
            print(f"  ID: {usuario.get('id')}, Nombre: {usuario.get('nombre')}, Email: {usuario.get('email')}")
    else:
        print(datos_leidos)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo_json}' no fue encontrado.")
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON (archivo mal formado?): {e}")
except IOError as e:
    print(f"Error al leer archivo JSON: {e}")

print("-" * 20)