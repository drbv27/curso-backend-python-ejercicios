# archivo: clase7_archivos.py

NOMBRE_ARCHIVO_EJEMPLO = "mi_documento_clase7.txt"

print(f"--- Escribiendo en '{NOMBRE_ARCHIVO_EJEMPLO}' con 'with open' ---")
try:
    # Modo 'w': crea o sobrescribe
    with open(NOMBRE_ARCHIVO_EJEMPLO, "w") as archivo_salida:
        archivo_salida.write("Primera línea de mi documento.\n")
        archivo_salida.write("Python es genial para manejar archivos.\n")
        archivo_salida.write(f"Podemos escribir números también (como str): {12345}\n")
    print(f"Archivo '{NOMBRE_ARCHIVO_EJEMPLO}' escrito con éxito.")

    # Modo 'a': añade al final
    with open(NOMBRE_ARCHIVO_EJEMPLO, "a") as archivo_salida:
        archivo_salida.write("Esta línea se añadió después.\n")
    print("Línea añadida con éxito.")
except IOError as e:
    print(f"Error de E/S al escribir: {e}")
print("-" * 20)


print(f"\n--- Leyendo '{NOMBRE_ARCHIVO_EJEMPLO}' con 'with open' ---")
try:
    print("\nContenido leído con read():")
    with open(NOMBRE_ARCHIVO_EJEMPLO, "r") as archivo_entrada:
        contenido_completo = archivo_entrada.read()
        print(contenido_completo)
    print("--- Fin read() ---")


    print("\nContenido leído línea por línea (con readline() en bucle):")
    with open(NOMBRE_ARCHIVO_EJEMPLO, "r") as archivo_entrada:
        linea = archivo_entrada.readline()
        while linea: # readline() devuelve string vacío '' al final del archivo
            print(linea.strip(), end=" <-readline\n") # strip() quita \n y espacios
            linea = archivo_entrada.readline()
    print("--- Fin readline() en bucle ---")


    print("\nContenido leído con readlines():")
    with open(NOMBRE_ARCHIVO_EJEMPLO, "r") as archivo_entrada:
        lista_de_lineas = archivo_entrada.readlines()
        print(f"Tipo de dato: {type(lista_de_lineas)}, Contenido: {lista_de_lineas}")
        for i, l_item in enumerate(lista_de_lineas):
            print(f"Línea {i}: {l_item.strip()}")
    print("--- Fin readlines() ---")


    print("\nContenido iterando sobre el archivo (recomendado):")
    with open(NOMBRE_ARCHIVO_EJEMPLO, "r") as archivo_entrada:
        for num_linea, linea_iterable in enumerate(archivo_entrada, 1):
            print(f"{num_linea}. {linea_iterable.strip()}")
    print("--- Fin iteración ---")

except FileNotFoundError:
    print(f"Error: El archivo '{NOMBRE_ARCHIVO_EJEMPLO}' no se encontró para leer.")
except IOError as e:
    print(f"Error de E/S al leer: {e}")
print("-" * 20)