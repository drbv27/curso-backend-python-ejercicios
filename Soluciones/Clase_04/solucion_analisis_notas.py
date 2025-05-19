# Solución Tarea Clase 4: Análisis de Notas (Conteo)

print("--- Análisis de Notas ---")
notas_curso = [4.5, 8.0, 3.2, 10.0, 6.7, 5.0, 2.0, 7.8, 9.1, 4.9, 5.0]
print(f"Notas del curso: {notas_curso}")

aprobados = 0
reprobados = 0
nota_aprobacion = 5.0

if not notas_curso: # Verificar si la lista está vacía
    print("No hay notas para analizar.")
else:
    for nota in notas_curso:
        if nota >= nota_aprobacion:
            aprobados += 1
        else:
            reprobados += 1

    print(f"\nResultados del Análisis (Nota de aprobación: {nota_aprobacion}):")
    print(f"Total de estudiantes: {len(notas_curso)}")
    print(f"Estudiantes Aprobados: {aprobados}")
    print(f"Estudiantes Reprobados: {reprobados}")

    if len(notas_curso) > 0:
        porcentaje_aprobados = (aprobados / len(notas_curso)) * 100
        print(f"Porcentaje de Aprobación: {porcentaje_aprobados:.2f}%")
print("-" * 20)