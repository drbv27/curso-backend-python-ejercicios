# archivo: clase5_practica.py

# Ejercicio 1: Diccionario de Producto
print("--- Ejercicio 1: Diccionario de Producto ---")
producto = {
    "nombre": "Laptop Gamer X",
    "precio": 1250.75,
    "stock": 15,
    "tags": ["gamer", "computador", "alto rendimiento"]
}
print(f"Diccionario original: {producto}")

# Imprimir precio
print(f"Precio: ${producto.get('precio', 0.0)}") # Usar get para seguridad

# Añadir marca
producto["marca"] = "TechPro"
print(f"Con marca: {producto}")

# Actualizar stock
if "stock" in producto:
    producto["stock"] -= 2 # o producto["stock"] = producto["stock"] - 2
print(f"Stock actualizado: {producto.get('stock', 'No disponible')}")

# Iterar e imprimir
print("\nDetalles del Producto:")
for clave, valor in producto.items():
    # Formateo simple de la clave para mejor lectura
    clave_formateada = clave.replace('_',' ').capitalize()
    print(f"- {clave_formateada}: {valor}")
print("-" * 20)


# Ejercicio 2: Conjuntos - Operaciones y Duplicados
print("--- Ejercicio 2: Conjuntos ---")
# Parte 1: Eliminar duplicados
numeros_con_duplicados = [10, 20, 30, 20, 40, 10, 50, 30, 30]
print(f"Lista original: {numeros_con_duplicados}")
numeros_sin_duplicados = set(numeros_con_duplicados)
print(f"Conjunto sin duplicados: {numeros_sin_duplicados}")
# Si necesitas una lista sin duplicados: list(numeros_sin_duplicados)

print("\nParte 2: Operaciones de conjuntos")
grupo_a = {1, 2, 3, 4, 5}
grupo_b = {4, 5, 6, 7, 8}
print(f"Grupo A: {grupo_a}")
print(f"Grupo B: {grupo_b}")

union_ab = grupo_a.union(grupo_b) # o grupo_a | grupo_b
print(f"Unión (A | B): {union_ab}")

interseccion_ab = grupo_a.intersection(grupo_b) # o grupo_a & grupo_b
print(f"Intersección (A & B): {interseccion_ab}")

diferencia_a_b = grupo_a.difference(grupo_b) # o grupo_a - grupo_b
print(f"Diferencia (A - B): {diferencia_a_b}")

diferencia_b_a = grupo_b.difference(grupo_a) # o grupo_b - grupo_a
print(f"Diferencia (B - A): {diferencia_b_a}")

diferencia_simetrica = grupo_a.symmetric_difference(grupo_b) # o grupo_a ^ grupo_b
print(f"Diferencia Simétrica (A ^ B): {diferencia_simetrica}")
print("-" * 20)