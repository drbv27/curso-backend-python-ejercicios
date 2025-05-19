# archivo: clase6_return.py

print("--- Funciones con return ---")
def sumar_y_devolver(num1, num2):
    resultado_interno = num1 + num2
    return resultado_interno

suma_calculada = sumar_y_devolver(20, 25)
print(f"El resultado devuelto es: {suma_calculada}")
print(f"Podemos usarlo directamente: {sumar_y_devolver(3, 4) * 10}")
print("-" * 20)


print("--- Funciones sin return explícito (devuelven None) ---")
def solo_imprime_saludo(nombre):
    print(f"Un saludo para {nombre}")
    # No hay return explícito

valor_recibido = solo_imprime_saludo("Elena")
print(f"La función 'solo_imprime_saludo' devolvió: {valor_recibido}")
print(f"Tipo de valor_recibido: {type(valor_recibido)}")
print("-" * 20)


print("--- Múltiples returns (en condicionales) ---")
def obtener_abs(numero):
    if numero < 0:
        return -numero
    # else: # El else es implícito si la condición anterior tiene return
    return numero

print(f"Valor absoluto de -5: {obtener_abs(-5)}")
print(f"Valor absoluto de 5: {obtener_abs(5)}")
print("-" * 20)


print("--- Retornando Múltiples Valores (como tupla) ---")
def obtener_dimensiones_rectangulo():
    base = 10.5
    altura = 5.2
    unidad_medida = "cm"
    return base, altura, unidad_medida # Retorna la tupla (10.5, 5.2, "cm")

dimensiones = obtener_dimensiones_rectangulo()
print(f"Dimensiones (tupla): {dimensiones}")
print(f"Tipo de dimensiones: {type(dimensiones)}")

# Se puede desempaquetar directamente
b, h, unidad = obtener_dimensiones_rectangulo()
print(f"Base: {b}{unidad}, Altura: {h}{unidad}")
print("-" * 20)