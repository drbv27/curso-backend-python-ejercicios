# archivo: clase6_practica.py

# Ejercicio 1: Área de Rectángulo
def calcular_area_rectangulo(base, altura):
    """Calcula y retorna el área de un rectángulo.

    Args:
        base (float): La longitud de la base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área calculada del rectángulo.
        str: Mensaje de error si base o altura no son positivos.
    """
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        return "Error: La base y la altura deben ser números."
    if base < 0 or altura < 0:
        return "Error: La base y la altura deben ser valores positivos."
    return base * altura

print("--- Ejercicio 1: Área Rectángulo ---")
try:
    b_usuario = float(input("Introduce la base del rectángulo: "))
    h_usuario = float(input("Introduce la altura del rectángulo: "))
    area_calculada = calcular_area_rectangulo(b_usuario, h_usuario)

    if isinstance(area_calculada, str): # Si retornó un mensaje de error
        print(area_calculada)
    else:
        print(f"El área del rectángulo es: {area_calculada:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, introduce números para base y altura.")
print("-" * 20)


# Ejercicio 2: ¿Es Par?
def es_par(numero):
    """Verifica si un número entero es par.

    Args:
        numero (int): El número a verificar.

    Returns:
        bool: True si el número es par, False en caso contrario.
        str: Mensaje de error si no es un entero.
    """
    if not isinstance(numero, int):
        return "Error: La entrada debe ser un número entero."
    return numero % 2 == 0

print("--- Ejercicio 2: ¿Es Par? ---")
try:
    num_ingresado = int(input("Introduce un número entero: "))
    resultado_par = es_par(num_ingresado)
    if isinstance(resultado_par, str):
        print(resultado_par)
    elif resultado_par: # es_par devolvió True
        print(f"El número {num_ingresado} es PAR.")
    else: # es_par devolvió False
        print(f"El número {num_ingresado} es IMPAR.")
except ValueError:
    print("Entrada inválida. Por favor, introduce un número entero.")
print("-" * 20)


# Ejercicio 3: Sumar Elementos de una Lista
def sumar_elementos_lista(lista_de_numeros):
    """Suma todos los números en una lista.

    Args:
        lista_de_numeros (list): Una lista que contiene números (int o float).

    Returns:
        float or int: La suma de los elementos de la lista. 0 si la lista está vacía.
                      None si la lista contiene elementos no numéricos.
    """
    suma_total = 0
    for elemento in lista_de_numeros:
        if not isinstance(elemento, (int, float)):
            print(f"Advertencia: Elemento no numérico '{elemento}' encontrado en la lista. Será ignorado.")
            continue # Opcional: podrías retornar un error o None
        suma_total += elemento
    return suma_total

print("--- Ejercicio 3: Sumar Lista ---")
mis_numeros = [10, 2.5, -5, 100, 7]
print(f"La lista es: {mis_numeros}")
total_suma_lista = sumar_elementos_lista(mis_numeros)
print(f"La suma de sus elementos es: {total_suma_lista}")

lista_vacia = []
print(f"\nLa lista vacía es: {lista_vacia}")
print(f"Suma de lista vacía: {sumar_elementos_lista(lista_vacia)}")

lista_con_error = [1, 2, "texto", 4]
print(f"\nLista con error: {lista_con_error}")
print(f"Suma de lista con error: {sumar_elementos_lista(lista_con_error)}")
print("-" * 20)