# archivo: clase4_practica.py

# Ejercicio 1: Análisis de Números en Lista
print("--- Ejercicio 1: Análisis de Números ---")
notas = [7.5, 9.0, 4.2, 8.8, 5.0, 6.0]
print(f"Lista de notas: {notas}")

suma_notas = 0.0 # Usar float para acumulador
for nota in notas:
    suma_notas += nota

# Calcular promedio solo si hay elementos
if len(notas) > 0:
    promedio = suma_notas / len(notas)
else:
    promedio = 0.0

print(f"Suma total: {suma_notas:.2f}") # Formatear a 2 decimales
print(f"Promedio: {promedio:.2f}")
print(f"Cantidad de notas: {len(notas)}")
if len(notas) > 0: # Evitar error si la lista está vacía
    print(f"Nota mínima: {min(notas)}")
    print(f"Nota máxima: {max(notas)}")
print("-" * 20)


# Ejercicio 2: Buscando en una Lista de Palabras
print("--- Ejercicio 2: Lista de Invitados ---")
invitados = ["Carlos", "Ana", "Eva", "Luis"]
print(f"Lista inicial de invitados: {invitados}")

nombre_usuario = input("Ingresa tu nombre: ").capitalize() # Capitalizamos para consistencia

if nombre_usuario in invitados:
    print(f"¡Bienvenido/a, {nombre_usuario}!")
else:
    print(f"Lo siento {nombre_usuario}, no estás en la lista.")
    # Bonus: Añadirlo
    print("Te añadiremos a la lista para la próxima.")
    invitados.append(nombre_usuario)
    print(f"Lista actualizada: {invitados}")
print("-" * 20)


# Ejercicio 3: Trabajando con Tuplas (Coordenadas)
print("--- Ejercicio 3: Tupla de Configuración ---")
punto_inicial = (150, 75) # Coordenadas X, Y
print(f"Punto inicial (tupla): {punto_inicial}")

# Imprimir la coordenada X y la coordenada Y usando índices.
print(f"Coordenada X: {punto_inicial[0]}")
print(f"Coordenada Y: {punto_inicial[1]}")

# Intenta modificar la coordenada X (esto generará un TypeError)
print("Intentando modificar la tupla...")
try:
    punto_inicial[0] = 100
except TypeError as e:
    print(f"ERROR: {e} (¡Como era de esperar, las tuplas son inmutables!)")

# Desempaqueta la tupla en dos variables coord_x e coord_y e imprímelas.
coord_x, coord_y = punto_inicial
print(f"Desempaquetado -> Coordenada X: {coord_x}, Coordenada Y: {coord_y}")
print("-" * 20)