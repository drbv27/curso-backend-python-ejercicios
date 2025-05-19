# archivo: clase4_tuplas.py

# Creación de Tuplas
print("--- Creación de Tuplas ---")
punto_2d = (10, 20)
colores_rgb = ("rojo", "verde", "azul")
datos_persona = ("Ana", 30, True, "Medellín")
tupla_vacia = ()
print(f"Punto 2D: {punto_2d}")
print(f"Colores RGB: {colores_rgb}")
print(f"Datos Persona: {datos_persona}")
print(f"Tupla Vacía: {tupla_vacia}")

# Tupla desde lista
tupla_desde_lista = tuple([10, 20, 30])
print(f"Tupla desde lista: {tupla_desde_lista}")

# ¡Tupla de un solo elemento!
no_es_tupla = (50)
print(f"Esto NO es tupla: {no_es_tupla}, tipo: {type(no_es_tupla)}")
si_es_tupla = (50,) # La coma es la clave
print(f"Esto SÍ es tupla: {si_es_tupla}, tipo: {type(si_es_tupla)}")
print("-" * 20)

# Acceso por Índice y Slicing (igual que listas)
print("--- Acceso y Slicing en Tuplas ---")
mi_tupla = (0, 10, 20, 30, 40, 50)
print(f"Original: {mi_tupla}")
print(f"mi_tupla[0]: {mi_tupla[0]}")
print(f"mi_tupla[-1]: {mi_tupla[-1]}")
print(f"mi_tupla[1:4]: {mi_tupla[1:4]}") # Devuelve una NUEVA tupla
print(f"mi_tupla[::-1]: {mi_tupla[::-1]}") # Devuelve una NUEVA tupla
print("-" * 20)

# Inmutabilidad
print("--- Inmutabilidad de las Tuplas ---")
# Las siguientes líneas generarían TypeError si se descomentan:
# mi_tupla[0] = 100
# mi_tupla.append(60) # AttributeError, no existe append
# del mi_tupla[0]     # TypeError
print("No se pueden modificar elementos, añadir o eliminar después de creadas.")
print("-" * 20)

# Operaciones con Tuplas
print("--- Operaciones ---")
t1 = (1, 2)
t2 = ("a", "b")
print(f"Concatenar: {t1 + t2}") # Devuelve NUEVA tupla: (1, 2, 'a', 'b')
print(f"Repetir: {t1 * 3}")   # Devuelve NUEVA tupla: (1, 2, 1, 2, 1, 2)
print(f"'a' in t2? {'a' in t2}")
print("-" * 20)

# Funciones Útiles
print("--- Funciones Útiles ---")
numeros_t = (10, 5, 25, 15, 5)
print(f"Tupla: {numeros_t}")
print(f"len(): {len(numeros_t)}")
print(f"min(): {min(numeros_t)}")
print(f"max(): {max(numeros_t)}")
print(f"sum(): {sum(numeros_t)}")
print(f"count(5): {numeros_t.count(5)}") # Tuplas sí tienen count e index
print(f"index(25): {numeros_t.index(25)}")
print("-" * 20)

# Bucle for con Tupla
print("--- Bucle for con Tupla ---")
config = ("localhost", 8080, True)
for valor in config:
    print(f"Valor de config: {valor}")
print("-" * 20)

# Desempaquetado de Tuplas
print("--- Desempaquetado ---")
coordenada = (1920, 1080)
ancho, alto = coordenada
print(f"Ancho: {ancho}, Alto: {alto}")

# Esto también funciona con listas y en bucles for
puntos_lista = [(0,0), (10,5), (20,15)]
for x_coord, y_coord in puntos_lista:
    print(f"Punto: X={x_coord}, Y={y_coord}")