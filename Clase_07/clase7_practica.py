# archivo: clase7_practica.py

# Para el Ejercicio 1, primero asegúrate de tener el archivo mi_modulo_calculos.py
# en la misma carpeta (Clase_07) con el siguiente contenido:
#
# # archivo: mi_modulo_calculos.py
# """Módulo simple de cálculos geométricos."""
# def area_triangulo(base, altura):
#     """Calcula el área de un triángulo."""
#     return (base * altura) / 2
#
# def perimetro_cuadrado(lado):
#     """Calcula el perímetro de un cuadrado."""
#     return 4 * lado
#
# if __name__ == "__main__":
#     print("Probando area_triangulo(10, 5):", area_triangulo(10, 5))
#     print("Probando perimetro_cuadrado(4):", perimetro_cuadrado(4))
# --- Fin de mi_modulo_calculos.py ---

print("--- Ejercicio 1: Usando mi_modulo_calculos ---")
try:
    # from mi_modulo_calculos import area_triangulo, perimetro_cuadrado # Opción 1
    import mi_modulo_calculos as mmc # Opción 2 (preferida si hay varias funciones)

    base_tri = float(input("Base del triángulo: "))
    altura_tri = float(input("Altura del triángulo: "))
    # print(f"Área del triángulo: {area_triangulo(base_tri, altura_tri)}") # Opción 1
    print(f"Área del triángulo: {mmc.area_triangulo(base_tri, altura_tri)}") # Opción 2

    lado_cuad = float(input("Lado del cuadrado: "))
    # print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado_cuad)}") # Opción 1
    print(f"Perímetro del cuadrado: {mmc.perimetro_cuadrado(lado_cuad)}") # Opción 2

except ImportError:
    print("Error: No se pudo importar 'mi_modulo_calculos.py'. Asegúrate de que exista.")
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
print("-" * 20)


print("--- Ejercicio 2: Cálculo de Edad Seguro ---")
import datetime
año_actual = datetime.datetime.now().year

try:
    año_nac_str = input("Introduce tu año de nacimiento: ")
    año_nac = int(año_nac_str)

    if año_nac > año_actual:
        print("Error: El año de nacimiento no puede ser en el futuro.")
    elif año_nac < año_actual - 130: # Límite de edad razonable
        print("Error: Año de nacimiento demasiado antiguo.")
    else:
        edad_aprox = año_actual - año_nac
        print(f"Tienes aproximadamente {edad_aprox} años.")
except ValueError:
    print("Error: Debes ingresar un año válido (número entero).")
except Exception as e:
    print(f"Ocurrió un error general: {e}")
finally:
    print("Verificación de edad finalizada.")
print("-" * 20)


print("--- Ejercicio 3: Lista de Tareas en Archivo ---")
nombre_archivo_pr_tareas = "mis_tareas_practica.txt"

# Escribir tareas
try:
    with open(nombre_archivo_pr_tareas, "w") as f_tareas_pr: # 'w' para sobrescribir
        print("Introduce 3 tareas pendientes para tu lista:")
        for i in range(3):
            tarea = input(f"Tarea {i+1}: ").strip()
            if tarea: # Solo escribir si no está vacía
                f_tareas_pr.write(tarea + "\n")
    print(f"Tareas guardadas en '{nombre_archivo_pr_tareas}'")
except IOError as e_io:
    print(f"Error al escribir en el archivo '{nombre_archivo_pr_tareas}': {e_io}")
except Exception as e_gen:
    print(f"Error inesperado al escribir: {e_gen}")


# Leer y mostrar tareas
print("\n--- Tareas Pendientes Leídas del Archivo ---")
try:
    with open(nombre_archivo_pr_tareas, "r") as f_lectura_pr:
        print(f"Contenido de '{nombre_archivo_pr_tareas}':")
        tareas_leidas = 0
        for i, linea_tarea in enumerate(f_lectura_pr, 1):
            print(f"{i}. {linea_tarea.strip()}")
            tareas_leidas += 1
        if tareas_leidas == 0:
             print("(No hay tareas en el archivo o está vacío).")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo_pr_tareas}' no fue encontrado.")
except IOError as e_io_read:
    print(f"Error al leer el archivo '{nombre_archivo_pr_tareas}': {e_io_read}")
except Exception as e_gen_read:
    print(f"Error inesperado al leer: {e_gen_read}")
print("-" * 20)