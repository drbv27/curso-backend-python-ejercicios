# 🛍️ Clase 4: Listas y Tuplas - Colecciones Ordenadas

En esta clase exploramos las primeras estructuras de datos para agrupar múltiples elementos: ¡las listas y las tuplas!

## ✅ Temas Cubiertos

* Introducción a las **Colecciones** y su necesidad.
* **Listas (`list`):**
    * Definición: Colecciones ordenadas, **mutables** y heterogéneas.
    * Creación: Con corchetes `[]` o `list()`.
    * Acceso: Por **índice** (base 0, índices negativos `[-1]`). `IndexError`.
    * **Slicing (Rebanadas)**: `lista[inicio:fin:paso]` para obtener sub-listas.
    * **Mutabilidad**:
        * Modificar elementos: `lista[indice] = nuevo_valor`.
        * Añadir: `append(el)`, `insert(idx, el)`.
        * Eliminar: `remove(val)`, `pop(idx_opc)`, `del lista[idx]`.
        * Reordenar: `sort()` (in-place), `reverse()` (in-place), `sorted(lista)` (nueva lista).
    * Operaciones: Concatenación (`+`), repetición (`*`), pertenencia (`in`, `not in`).
    * Funciones: `len()`, `min()`, `max()`, `sum()`.
* **Tuplas (`tuple`):**
    * Definición: Colecciones ordenadas, **INMUTABLES** y heterogéneas.
    * Creación: Con paréntesis `()` o `tuple()`. ¡Caso especial: `(elemento,)` para un solo ítem!
    * Acceso y Slicing: Igual que las listas.
    * **Inmutabilidad**: ¡No se pueden cambiar! Intentarlo produce `TypeError`.
    * Operaciones y Funciones: Similares a listas (pero `+` y `*` crean nuevas tuplas).
    * **Desempaquetado**: `x, y = mi_tupla`.
* **Comparación**: Cuándo usar Listas vs. Tuplas.

## 💻 Archivos de Código

* [`clase4_listas.py`](./clase4_listas.py): Ejemplos detallados sobre creación, acceso, slicing, métodos de modificación y operaciones con Listas.
* [`clase4_tuplas.py`](./clase4_tuplas.py): Ejemplos detallados sobre creación (incluyendo tupla de un solo elemento), acceso, slicing, demostración de inmutabilidad, operaciones y desempaquetado de Tuplas.
* [`clase4_practica.py`](./clase4_practica.py): Soluciones a los ejercicios prácticos realizados en clase (Análisis de notas en lista, Búsqueda en lista de invitados, Trabajo con tupla de coordenadas).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Lista de Compras Interactiva:**
    * Crea un script que simule una lista de compras.
    * Usa un bucle `while True:` y `input()` para presentar un menú al usuario con opciones:
        1.  Añadir ítem
        2.  Eliminar ítem
        3.  Ver lista
        4.  Salir
    * Implementa la lógica para cada opción usando una lista y sus métodos (`append`, `remove`, etc.).
    * Para "Ver lista", si está vacía, muestra un mensaje. Si no, muestra los ítems (quizás numerados usando `enumerate` dentro de un bucle `for`).
2.  **Análisis de Notas Avanzado:**
    * Dada una lista de notas numéricas (ej: `[4.5, 8.0, 3.2, 10.0, 6.7, 5.0, 2.0, 7.8, 9.1, 4.9, 5.0]`).
    * Calcula y muestra:
        * Número total de notas.
        * Nota promedio.
        * Nota más alta y más baja.
        * Cantidad de estudiantes aprobados (nota >= 5.0) y reprobados.
        * Porcentaje de aprobación.
    * *(Bonus)* Permite al usuario ingresar las notas una por una hasta que ingrese un valor específico para terminar (ej: -1).

---
*Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_04/`.*