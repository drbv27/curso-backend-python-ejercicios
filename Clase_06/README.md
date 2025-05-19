# 🛠️ Clase 6: Funciones - Bloques de Código Reutilizables

¡Las funciones son uno de los pilares de la programación estructurada y el principio DRY (Don't Repeat Yourself)! En esta clase, aprendemos a crear nuestros propios bloques de código con nombre.

## ✅ Temas Cubiertos

- **¿Qué son las Funciones?**: Bloques de código con nombre para realizar tareas específicas.
- **Beneficios**: DRY, modularidad, reutilización, legibilidad.
- **Definición**: Uso de `def nombre_funcion():`, dos puntos `:` y cuerpo **indentado**. `pass` como placeholder.
- **Llamada (Invocación)**: `nombre_funcion()`.
- **Parámetros y Argumentos**:
  - **Parámetros**: Variables en la definición de la función (dentro de `()`).
  - **Argumentos**: Valores pasados al llamar la función.
  - **Argumentos Posicionales**: El orden de los argumentos importa.
  - **Argumentos Nombrados (Keyword Arguments)**: `parametro=valor`. El orden no importa si se nombran. Claridad.
- **Valores de Retorno (`return`)**:
  - Cómo una función devuelve un resultado al código que la llamó.
  - `return valor_o_expresion`. La función termina inmediatamente.
  - Si no hay `return` explícito (o `return` solo), la función devuelve `None`.
  - Múltiples `return` en diferentes ramas condicionales.
  - Retornar múltiples valores (Python los empaqueta como una tupla).
- **Docstrings (Cadenas de Documentación)**:
  - `"""Docstring aquí..."""` como primera línea de la función.
  - Explican propósito, `Args` (parámetros) y `Returns` (lo que devuelve).
  - Accesibles con `help(funcion)` o `funcion.__doc__`.
- **Alcance de Variables (Scope)**:
  - **Variables Locales**: Definidas dentro de una función, solo existen ahí.
  - **Variables Globales**: Definidas fuera, legibles desde dentro.
  - Palabra clave `global` para _modificar_ una global (usar con precaución).
- **Parámetros con Valores por Defecto**:
  - `def funcion(param, param_opcional="default")`.
  - Parámetros con default deben ir _después_ de los obligatorios.

## 💻 Archivos de Código

- [`clase6_funciones.py`](./clase6_funciones.py): Ejemplos de definición, llamada, parámetros y argumentos (posicionales y nombrados).
- [`clase6_return.py`](./clase6_return.py): Demostraciones de cómo las funciones retornan valores, incluyendo `None` y múltiples valores (tuplas).
- [`clase6_docstrings.py`](./clase6_docstrings.py): Ejemplo de cómo escribir y acceder a docstrings.
- [`clase6_scope.py`](./clase6_scope.py): Ilustración del alcance de variables locales y globales, y el uso de la palabra clave `global`.
- [`clase6_default_params.py`](./clase6_default_params.py): Ejemplos de funciones con parámetros que tienen valores por defecto.
- [`clase6_practica.py`](./clase6_practica.py): Soluciones a los ejercicios prácticos realizados en clase (Área Rectángulo, Es Par, Sumar Lista).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Factorial de un Número:**
    - Crea una función `factorial(n)` que reciba un entero no negativo `n`.
    - La función debe calcular y retornar el factorial de `n` (`n! = n * (n-1) * ... * 1`).
    - Considera que `0! = 1`.
    - Añade validación para números negativos o no enteros.
2.  **Verificador de Palíndromos:**
    - Crea una función `es_palindromo(palabra)` que reciba un string.
    - Debe retornar `True` si la `palabra` es un palíndromo (se lee igual al derecho y al revés, ej: "ana", "reconocer", "Luz azul").
    - Debe retornar `False` en caso contrario.
    - _Pista:_ Considera convertir la palabra a minúsculas (`.lower()`) y quizás eliminar espacios (`.replace(" ", "")`) para una comparación más robusta. `palabra[::-1]` invierte un string.
3.  **Búsqueda en Lista (Implementación Manual):**
    - Crea una función `buscar_en_lista(mi_lista, elemento_a_buscar)` que reciba una lista y un elemento.
    - La función debe retornar `True` si `elemento_a_buscar` se encuentra en `mi_lista`, y `False` si no.
    - **Importante:** Para practicar la lógica de bucles dentro de funciones, implementa esta búsqueda usando un bucle `for` y una comparación `if`, _sin_ usar el operador `in` directamente sobre la lista.

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_06/`._
