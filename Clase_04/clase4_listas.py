# archivo: clase4_listas.py

# Creación de Listas
print("--- Creación de Listas ---")
numeros = [10, 20, 30, 40, 50]
nombres = ["Ana", "Luis", "Eva"]
mixta = [100, "Python", True, 3.14]
lista_vacia = []
print(f"Números: {numeros}")
print(f"Nombres: {nombres}")
print(f"Mixta: {mixta}")
print(f"Vacía: {lista_vacia}")

otra_vacia = list()
letras_palabra = list("Hola") # -> ['H', 'o', 'l', 'a']
print(f"Desde string 'Hola': {letras_palabra}")
print("-" * 20)

# Acceso por Índice
print("--- Acceso por Índice ---")
print(f"Primer número: {numeros[0]}") # 10
print(f"Último nombre: {nombres[-1]}") # Eva
# print(numeros[10]) # IndexError
print("-" * 20)

# Slicing (Rebanadas)
print("--- Slicing ---")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {nums}")
print(f"nums[2:6]: {nums[2:6]}")     # [2, 3, 4, 5]
print(f"nums[:3]: {nums[:3]}")      # [0, 1, 2]
print(f"nums[4:]: {nums[4:]}")      # [4, 5, 6, 7, 8, 9]
print(f"nums[::2]: {nums[::2]}")    # [0, 2, 4, 6, 8]
print(f"nums[::-1]: {nums[::-1]}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
copia = nums[:]
print(f"Copia: {copia}")
print("-" * 20)

# Modificación de Listas
print("--- Modificando Listas ---")
colores = ["rojo", "verde", "azul"]
print(f"Antes: {colores}")
colores[1] = "amarillo"
print(f"Cambio: {colores}")
colores.append("naranja")
print(f"Append: {colores}")
colores.insert(1, "violeta")
print(f"Insert: {colores}")
colores.remove("amarillo")
print(f"Remove 'amarillo': {colores}")
el_pop = colores.pop(2)
print(f"Pop(2) -> {el_pop}, Lista: {colores}")
del colores[0]
print(f"Del [0]: {colores}")
print("-" * 20)

# Reordenar Listas
print("--- Reordenando Listas ---")
numeros_desordenados = [5, 1, 4, 2, 8]
print(f"Desordenados: {numeros_desordenados}")
numeros_desordenados.sort()
print(f"sort(): {numeros_desordenados}")
numeros_desordenados.sort(reverse=True)
print(f"sort(reverse=True): {numeros_desordenados}")
numeros_desordenados.reverse()
print(f"reverse(): {numeros_desordenados}")

mas_numeros = [60, 10, 90, 30]
ordenada_nueva = sorted(mas_numeros)
print(f"sorted({mas_numeros}): {ordenada_nueva}")
print(f"Original no cambia: {mas_numeros}")
print("-" * 20)

# Operaciones con Listas
print("--- Operaciones ---")
lista_a = [1, 2]
lista_b = [3, 4]
print(f"Concatenar: {lista_a + lista_b}")
print(f"Repetir: {lista_a * 3}")
print(f"2 in {lista_a}? {2 in lista_a}")
print("-" * 20)

# Funciones Útiles
print("--- Funciones Útiles ---")
mi_lista = [10, 5, 25, 15, 5]
print(f"Lista: {mi_lista}")
print(f"len(): {len(mi_lista)}")
print(f"min(): {min(mi_lista)}")
print(f"max(): {max(mi_lista)}")
print(f"sum(): {sum(mi_lista)}")
# Métodos que no hemos visto pero son útiles:
print(f"count(5): {mi_lista.count(5)}") # Cuenta cuántas veces aparece el 5
print(f"index(25): {mi_lista.index(25)}") # Devuelve el índice de la primera ocurrencia de 25
print("-" * 20)

# Bucle for con Lista
print("--- Bucle for con Lista ---")
frutas = ["manzana", "pera", "banana"]
for fruta in frutas:
    print(f"Me gusta la {fruta.capitalize()}")