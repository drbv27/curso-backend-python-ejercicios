# archivo: clase5_conjuntos.py

print("--- Creando Conjuntos ---")
numeros_set = {1, 2, 3, 4, 5, 2, 3} # Duplicados se ignoran
print(f"Conjunto de números: {numeros_set}")

# Conjunto vacío DEBE ser con set()
conjunto_vacio = set()
print(f"Conjunto vacío: {conjunto_vacio}, tipo: {type(conjunto_vacio)}")

lista_duplicados = [10, 20, 10, 30, 20, 20, 40]
set_desde_lista = set(lista_duplicados)
print(f"Conjunto desde lista (sin duplicados): {set_desde_lista}")
print("-" * 20)


print("--- Añadir y Eliminar Elementos ---")
mis_frutas = {"manzana", "pera"}
mis_frutas.add("naranja")
mis_frutas.add("pera") # No cambia, ya existe
print(f"Frutas: {mis_frutas}")

mis_frutas.remove("pera")
# mis_frutas.remove("mango") # KeyError
print(f"Después de remove('pera'): {mis_frutas}")

mis_frutas.discard("naranja")
mis_frutas.discard("mango") # No da error
print(f"Después de discard('naranja') y discard('mango'): {mis_frutas}")

mis_frutas.update({"kiwi", "fresa", "uva"}) # Añade múltiples elementos
print(f"Después de update: {mis_frutas}")
if mis_frutas: # Si no está vacío
    elemento_pop = mis_frutas.pop()
    print(f"Elemento con pop(): {elemento_pop}, conjunto ahora: {mis_frutas}")
print("-" * 20)


print("--- Operaciones de Conjuntos ---")
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")

print(f"Unión (A | B): {set_A | set_B}")
print(f"Intersección (A & B): {set_A & set_B}")
print(f"Diferencia (A - B): {set_A - set_B}")
print(f"Diferencia Simétrica (A ^ B): {set_A ^ set_B}")
print("-" * 20)


print("--- Pertenencia y Longitud ---")
print(f"¿Está 3 en Set A? {3 in set_A}")
print(f"Longitud de (A | B): {len(set_A | set_B)}")
print("-" * 20)

print("--- Iterando sobre Conjuntos ---")
for item in set_A | set_B: # Iterar sobre la unión
    print(item, end=" ")
print("\n" + "-" * 20)


print("--- Eliminar duplicados de una lista ---")
mi_lista = [1,1,1,2,2,3,4,4,5]
lista_sin_duplicados = list(set(mi_lista))
print(f"Lista original: {mi_lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")