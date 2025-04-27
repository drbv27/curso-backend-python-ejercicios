# 🏁 Clase 1: Introducción y Fundamentos Básicos de Python

¡Bienvenidos a la primera parada de nuestro viaje! En esta clase sentamos las bases esenciales.

## ✅ Temas Cubiertos

- Introducción conceptual a la **programación** y al **desarrollo backend**.
- Instalación y configuración de **Python** y **Visual Studio Code (VS Code)**.
- Tu primer script: `print("Hola Mundo")` y cómo ejecutarlo.
- **Comentarios** en Python (`#`).
- **Variables**: Qué son, reglas de nombrado (`snake_case`) y asignación (`=`).
- **Tipos de Datos Fundamentales**:
  - `int` (Enteros)
  - `float` (Decimales - ¡con punto!)
  - `str` (Texto - ¡entre comillas!)
  - `bool` (Booleanos - `True` / `False` - ¡con mayúscula!)
  - Uso de la función `type()`.
- **Operadores Aritméticos**: `+`, `-`, `*`, `/`, `//` (división entera), `%` (módulo), `**` (potencia).
- **Operadores de Asignación**: `=`, `+=`, `-=`, `*=`, `/=`, etc.
- Entrada de usuario con `input()` y la **¡IMPORTANTE!** regla: siempre devuelve `str`.
- Salida de datos con `print()`.
- **Conversión de Tipos (Casting)**: `int()`, `float()`, `str()`.
- Formateo de cadenas moderno con **f-strings**: `f"Valor: {variable}"`.

## 💻 Archivos de Código

- [`clase1_hola.py`](./clase1_hola.py): Ejemplo básico de `print()` y comentarios.
- [`clase1_variables.py`](./clase1_variables.py): Demostración de variables, tipos de datos y `type()`.
- [`clase1_operadores.py`](./clase1_operadores.py): Ejemplos de operadores aritméticos y de asignación.
- [`clase1_practica.py`](./clase1_practica.py): Soluciones a los ejercicios prácticos realizados en clase (Saludo con edad, Calculadora de Rectángulo).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Conversor Celsius a Fahrenheit:**
    - Crea un script que pida al usuario una temperatura en grados Celsius.
    - Conviértela a Fahrenheit usando la fórmula: `F = (C * 9/5) + 32`.
    - Muestra el resultado claramente (ej: `"XX°C equivalen a YY.ZZ°F"`).
    - _Pista:_ Recuerda usar `float()` para la conversión de la entrada. Considera usar `try-except` (aunque aún no lo hemos visto formalmente) para manejar entradas no numéricas.
2.  **Experimentación y Errores:**
    - Modifica los scripts de ejemplo (`clase1_*.py`). Cambia valores, prueba operaciones.
    - Introduce errores _a propósito_: olvida comillas, usa un solo `=` para comparar (¡lo veremos en Clase 2!), intenta sumar un `str` y un `int` sin convertir...
    - Observa los mensajes de error que Python te da. ¡Aprender a leer e interpretar errores es una habilidad fundamental!

---

_Puedes encontrar una posible solución al ejercicio 1 (Conversor) en la carpeta `Soluciones/Clase_01/`._
