# Solución Tarea Clase 2: Validación de Nota (0-100) y Calificación

print("--- Calificación de Notas (con Validación) ---")
nota_str = input("Introduce tu nota (0-100): ")

try:
    nota = float(nota_str)

    # 1. Validación del Rango
    if nota < 0 or nota > 100:
        resultado = "Nota inválida (fuera de rango 0-100)"
    # 2. Clasificación (solo si la nota es válida)
    elif nota >= 90:
        resultado = "Sobresaliente"
    elif nota >= 70:
        resultado = "Notable"
    elif nota >= 50:
        resultado = "Aprobado"
    else: # Si es < 50 y >= 0
        resultado = "Suspenso"

    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: Entrada inválida. Debes introducir un número.")

print("-" * 20)