# 🧩 Clase 5: Diccionarios y Conjuntos - Colecciones Avanzadas

¡Ampliamos nuestro arsenal de estructuras de datos! Esta clase introduce los diccionarios para mapeos clave-valor y los conjuntos para elementos únicos.

## ✅ Temas Cubiertos

- Repaso de Listas y Tuplas.
- Introducción a colecciones no basadas en índices secuenciales.
- **Diccionarios (`dict`):**
  - Estructura **`clave:valor`**. Claves únicas e inmutables. Valores flexibles.
  - Son **mutables** y **ordenados** (desde Python 3.7, por orden de inserción).
  - Creación: Con llaves `{}` o `dict()`. Vacío: `{}`.
  - Acceso: `d['clave']` (riesgo de `KeyError`) o `d.get('clave', default_val)` (seguro).
  - Añadir/Modificar: `d['clave'] = nuevo_valor`.
  - Eliminar: `d.pop('clave')`, `del d['clave']`, `d.popitem()`.
  - Pertenencia: `'clave' in d`.
  - Vistas dinámicas: `d.keys()`, `d.values()`, `d.items()`.
  - Iteración: Sobre claves, valores, o (preferentemente) ítems `for k, v in d.items():`.
  - `len(d)`.
- **Conjuntos (`set`):**
  - Colección de elementos **ÚNICOS** e inmutables. El conjunto en sí es **mutable**.
  - Generalmente **desordenados** (no se debe confiar en el orden de iteración).
  - Creación: Con llaves `{elem1, elem2}` (si no es vacío), o `set(iterable)`.
  - **Conjunto Vacío: `s_vacio = set()` (¡NO `{}`!)**.
  - Añadir: `s.add(elemento)`.
  - Eliminar: `s.remove(elemento)` (`KeyError`), `s.discard(elemento)` (sin error), `s.pop()` (elemento arbitrario).
  - **Operaciones de Conjuntos**: Unión (`|`), Intersección (`&`), Diferencia (`-`), Diferencia Simétrica (`^`).
  - Pertenencia: `elemento in s` (muy eficiente). `len(s)`.
- Breve comparación: Listas vs. Tuplas vs. Diccionarios vs. Conjuntos.

## 💻 Archivos de Código

- [`clase5_diccionarios.py`](./clase5_diccionarios.py): Ejemplos detallados sobre creación, acceso, modificación, eliminación, vistas e iteración de Diccionarios.
- [`clase5_conjuntos.py`](./clase5_conjuntos.py): Ejemplos detallados sobre creación, añadir/eliminar elementos y operaciones fundamentales con Conjuntos.
- [`clase5_practica.py`](./clase5_practica.py): Soluciones a los ejercicios prácticos realizados en clase (Perfil de Usuario con diccionario, Ingredientes Comunes/Únicos con conjuntos).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Directorio Telefónico (Diccionario):**
    - Crea un diccionario para almacenar nombres (claves) y números de teléfono (valores).
    - Implementa un menú interactivo (`while` y `if/elif/else`) que permita al usuario:
      - Añadir un nuevo contacto (nombre y teléfono).
      - Buscar el teléfono de un contacto por su nombre.
      - Eliminar un contacto por su nombre.
      - Mostrar todos los contactos (nombre y teléfono).
      - Salir del programa.
2.  **Contador de Frecuencia de Palabras (Diccionario):**
    - Dada una frase (un string largo), cuenta cuántas veces aparece cada palabra.
    - El resultado debe ser un diccionario donde la clave es la palabra y el valor es su frecuencia (conteo).
    - _Pistas:_ Convierte la frase a minúsculas (`.lower()`). Divide la frase en una lista de palabras (`.split()`). Itera sobre la lista de palabras y actualiza el conteo en el diccionario. Considera eliminar signos de puntuación básicos.
3.  **Análisis de Tags (Conjuntos):**
    - Imagina dos artículos de blog. Cada uno tiene una lista de tags (etiquetas, strings).
    - `tags_blog1 = ["python", "desarrollo", "api", "backend"]`
    - `tags_blog2 = ["python", "django", "tutorial", "api"]`
    - Usando conjuntos, encuentra e imprime:
      - Los tags que ambos artículos tienen en común.
      - Todos los tags únicos utilizados entre ambos artículos.
      - Los tags que solo tiene el primer artículo pero no el segundo.
      - Los tags que solo tiene el segundo artículo pero no el primero.

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_05/`._
