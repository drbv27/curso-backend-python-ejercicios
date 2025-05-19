# Solución Tarea Clase 5: Tags en Común con Conjuntos

print("--- Análisis de Tags de Artículos ---")

tags_articulo1 = ["python", "programacion", "desarrollo web", "api", "backend"]
tags_articulo2 = ["python", "api", "django", "tutorial", "backend", "javascript"]

print(f"Tags Artículo 1: {tags_articulo1}")
print(f"Tags Artículo 2: {tags_articulo2}")

# Convertimos las listas a conjuntos para usar las operaciones de conjuntos
set_tags1 = set(tags_articulo1)
set_tags2 = set(tags_articulo2)

# 1. Tags que ambos artículos tienen en común (intersección)
tags_comunes = set_tags1.intersection(set_tags2) # o set_tags1 & set_tags2
print(f"\nTags comunes a ambos artículos: {tags_comunes}")

# 2. Todos los tags únicos usados entre ambos artículos (unión)
todos_los_tags = set_tags1.union(set_tags2) # o set_tags1 | set_tags2
print(f"Todos los tags únicos entre ambos: {todos_los_tags}")

# 3. Tags que solo tiene el artículo 1 pero no el segundo (diferencia)
tags_solo_en_1 = set_tags1.difference(set_tags2) # o set_tags1 - set_tags2
print(f"Tags solo en Artículo 1 (no en Artículo 2): {tags_solo_en_1}")

# (Extra) Tags que solo tiene el artículo 2 pero no el primero
tags_solo_en_2 = set_tags2.difference(set_tags1) # o set_tags2 - set_tags1
print(f"Tags solo en Artículo 2 (no en Artículo 1): {tags_solo_en_2}")

# (Extra) Tags que están en uno u otro pero no en ambos (diferencia simétrica)
tags_no_comunes_total = set_tags1.symmetric_difference(set_tags2) # o set_tags1 ^ set_tags2
print(f"Tags que están en un artículo o el otro, pero no en ambos: {tags_no_comunes_total}")

print("-" * 20)