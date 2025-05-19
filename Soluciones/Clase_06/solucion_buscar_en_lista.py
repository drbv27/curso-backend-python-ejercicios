# Solución Tarea Clase 6: Buscar Elemento en Lista (con bucle)

def esta_en_lista(mi_lista, elemento_a_buscar):
    """
    Verifica si un elemento está presente en una lista usando un bucle.

    Args:
        mi_lista (list): La lista donde buscar.
        elemento_a_buscar: El elemento que se desea encontrar.

    Returns:
        bool: True si el elemento se encuentra en la lista, False en caso contrario.
    """
    if not isinstance(mi_lista, list):
        print("Error: El primer argumento debe ser una lista.")
        return False # O manejar el error de otra forma

    encontrado = False
    for item in mi_lista:
        if item == elemento_a_buscar:
            encontrado = True
            break # Elemento encontrado, no es necesario seguir buscando
    return encontrado

print("--- Buscador de Elemento en Lista (con bucle) ---")
numeros = [10, 25, 5, 42, 18, 7]
nombres = ["Ana", "Luis", "Eva", "Juan"]

print(f"Lista de números: {numeros}")
print(f"¿Está el 42 en la lista? {esta_en_lista(numeros, 42)}") # True
print(f"¿Está el 100 en la lista? {esta_en_lista(numeros, 100)}") # False

print(f"\nLista de nombres: {nombres}")
print(f"¿Está 'Eva' en la lista? {esta_en_lista(nombres, 'Eva')}") # True
print(f"¿Está 'Pedro' en la lista? {esta_en_lista(nombres, 'Pedro')}") # False

print(f"Intentando buscar en algo que no es lista: {esta_en_lista('texto', 'e')}")
print("-" * 20)