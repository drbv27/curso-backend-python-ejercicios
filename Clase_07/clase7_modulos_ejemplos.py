# archivo: clase7_modulos_ejemplos.py

print("--- Usando el módulo mis_operaciones (import completo) ---")
import mis_operaciones
resultado_suma = mis_operaciones.sumar(10, 5)
print(f"Suma desde módulo: {resultado_suma}")
print(f"Valor de PI en el módulo: {mis_operaciones.PI}")
mis_operaciones.saludar_modulo()
print("-" * 20)


print("--- Usando el módulo mis_operaciones (from ... import) ---")
from mis_operaciones import sumar as suma_alias, PI as pi_constante
resultado_suma_directa = suma_alias(7, 3)
print(f"Suma directa con alias: {resultado_suma_directa}")
print(f"PI directo con alias: {pi_constante}")
# restar(10,2) # NameError: name 'restar' is not defined si no se importó
print("-" * 20)


print("--- Usando módulo math ---")
import math
print(f"Raíz cuadrada de 25: {math.sqrt(25)}")
print(f"Valor de pi (del módulo math): {math.pi}")
print("-" * 20)


print("--- Usando módulo random ---")
import random
numero_aleatorio = random.randint(1, 100)
print(f"Número aleatorio (1-100): {numero_aleatorio}")
opciones = ["piedra", "papel", "tijera"]
eleccion_pc = random.choice(opciones)
print(f"La PC eligió: {eleccion_pc}")
print("-" * 20)


print("--- Usando módulo datetime ---")
import datetime
ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Solo la fecha: {ahora.date()}")
print(f"Solo la hora: {ahora.time()}")
print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")
print(f"Fecha formateada: {ahora.strftime('%d/%m/%Y %H:%M')}")
print("-" * 20)