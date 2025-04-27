# 🤔 Clase 2: Estructuras de Control - Condicionales

¡En esta clase, nuestros programas empiezan a tomar decisiones! Aprendemos a controlar el flujo de ejecución.

## ✅ Temas Cubiertos

- Repaso rápido de la Clase 1.
- Introducción al **Control de Flujo**: ¿Por qué los programas necesitan decidir?
- **Operadores de Comparación**: `==` (¡no `=`!), `!=`, `<`, `>`, `<=`, `>=`. Evalúan a `True` o `False`.
- **Operadores Lógicos**: `and` (Y), `or` (O), `not` (NO). Para combinar condiciones booleanas.
- La Sentencia `if`: Ejecutar código si una condición es `True`.
- **¡INDENTACIÓN!**: La regla de oro en Python para definir bloques de código. ¡4 espacios!
- La Sentencia `if-else`: Elegir entre dos caminos (si `True` / si `False`).
- La Sentencia `if-elif-else`: Elegir entre múltiples caminos excluyentes.
- Mención a **Condicionales Anidados** ( `if` dentro de `if`).

## 💻 Archivos de Código

- [`clase2_comparacion.py`](./clase2_comparacion.py): Ejemplos de uso de operadores de comparación.
- [`clase2_logicos.py`](./clase2_logicos.py): Ejemplos de uso de operadores lógicos.
- [`clase2_if_simple.py`](./clase2_if_simple.py): Demostración básica de `if`.
- [`clase2_if_else.py`](./clase2_if_else.py): Demostración de `if-else` (Par/Impar, Mayoría de Edad).
- [`clase2_if_elif_else.py`](./clase2_if_elif_else.py): Demostración de `if-elif-else` (Clasificar Número, Saludo por Hora).
- [`clase2_practica.py`](./clase2_practica.py): Soluciones a los ejercicios prácticos realizados en clase (Mayoría Edad, Calificación Notas, Login Simple).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Validación de Nota Mejorada:**
    - Modifica la solución del Ejercicio 2 en `clase2_practica.py`.
    - Asegúrate de que el script **primero** comprueba si la nota introducida está en el rango `[0, 100]`.
    - Si no lo está, muestra "Nota inválida" y termina esa parte.
    - Si _sí_ está en el rango, entonces procede a la clasificación (Sobresaliente, Notable, etc.).
2.  **Feedback de Login Más Específico:**
    - Modifica la solución del Ejercicio 3 en `clase2_practica.py`.
    - En lugar de un solo mensaje de "Credenciales incorrectas", da un feedback más útil:
      - Si el `usuario_ingresado` no coincide con `usuario_correcto`, muestra "Usuario no encontrado."
      - Si el `usuario_ingresado` sí coincide, PERO la `password_ingresada` no coincide con `password_correcto`, muestra "Contraseña incorrecta."
      - Si ambos coinciden, muestra "Acceso concedido."
    - _Pista:_ Un `if` para el usuario y, _dentro_ de la parte verdadera de ese `if`, otro `if-else` para la contraseña (anidamiento) puede funcionar. O también puedes usar `elif`.
3.  **Calculadora con Menú:**
    - Crea un script nuevo que presente un menú:
      ```
      Calculadora Simple:
      1. Sumar
      2. Restar
      3. Multiplicar
      4. Dividir
      ```
    - Pida al usuario que elija una opción (`1`, `2`, `3` o `4`).
    - Pida al usuario dos números (`float` es recomendable).
    - Use `if-elif-else` para realizar la operación correspondiente a la opción elegida.
    - Muestre el resultado (ej. `"Resultado: 5 + 3 = 8"`).
    - Si el usuario elige una opción inválida (no 1, 2, 3 o 4), muestra un mensaje de error.
    - **¡Extra!** Maneja el caso de la división por cero (si el usuario elige dividir y el segundo número es 0).

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_02/`._
