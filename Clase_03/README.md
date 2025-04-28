# 🔁 Clase 3: Estructuras de Control - Bucles (`while` y `for`)

¡Es hora de automatizar! En esta clase aprendemos a repetir tareas usando los bucles de Python.

## ✅ Temas Cubiertos

- Repaso de Condicionales (`if`/`elif`/`else`).
- Introducción a los **Bucles**: Por qué y para qué repetir código.
- **Bucle `while`**:
  - Sintaxis: `while condicion:`
  - Ejecución basada en condición (`True`/`False`).
  - Elementos clave: Inicialización, Condición, **Actualización**.
  - ¡Peligro de **Bucles Infinitos** y cómo detenerlos (`Ctrl+C`)!
- Control de Flujo en Bucles:
  - **`break`**: Para salir inmediatamente del bucle.
  - **`continue`**: Para saltar al inicio de la siguiente iteración.
- **Bucle `for`**:
  - Sintaxis: `for variable in iterable:`
  - Iteración sobre elementos de una secuencia (iterables: `str`, `range`, listas, etc.).
- La función **`range()`**: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`.
- Combinación de **Bucles y Condicionales**.

## 💻 Archivos de Código

- [`clase3_while.py`](./clase3_while.py): Ejemplos de bucle `while` (contador, suma hasta 0).
- [`clase3_break_continue.py`](./clase3_break_continue.py): Demostración de `break` y `continue` dentro de `while`.
- [`clase3_for.py`](./clase3_for.py): Ejemplos de bucle `for` iterando sobre strings y usando `range()`. Muestra de `if` dentro de `for`.
- [`clase3_practica.py`](./clase3_practica.py): Soluciones a los ejercicios prácticos realizados en clase (Adivinar contraseña, Suma 1-100, Omitir múltiplos de 3).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Tabla de Multiplicar:**
    - Crea un script que pida al usuario un número entero.
    - Utiliza un bucle `for` y `range(1, 11)` para mostrar la tabla de multiplicar de ese número, del 1 al 10.
    - Formato de salida esperado: `N x 1 = R`, `N x 2 = R`, ..., `N x 10 = R`.
2.  **Juego "Adivina el Número":**
    - Importa el módulo `random` (`import random`).
    - Genera un número entero aleatorio entre 1 y 100 (`random.randint(1, 100)`).
    - Usa un bucle `while` para que el usuario intente adivinar el número.
    - En cada intento, indica si el número secreto es mayor o menor que el intento del usuario.
    - Si el usuario adivina, felicítalo, muestra cuántos intentos necesitó y termina el bucle (usa `break` o una variable booleana).
    - _(Bonus)_ Añade manejo de errores por si el usuario no introduce un número.

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_03/`._
