# Clase 2: Estructuras de Control - Condicionales

## Temas Cubiertos

- Repaso Clase 1.
- Introducción al Control de Flujo: la necesidad de tomar decisiones.
- Operadores de Comparación (`==`, `!=`, `<`, `>`, `<=`, `>=`) y resultados booleanos (`True`/`False`).
- Operadores Lógicos (`and`, `or`, `not`) para combinar condiciones.
- La sentencia `if` para ejecución condicional.
- **La importancia CRUCIAL de la INDENTACIÓN en Python.**
- La sentencia `if-else` para manejar alternativas.
- La sentencia `if-elif-else` para manejar múltiples condiciones excluyentes.
- Breve mención a condicionales anidados.

## Archivos de Código

- `clase2_comparacion.py`: Ejemplos de uso de operadores de comparación.
- `clase2_logicos.py`: Ejemplos de uso de operadores lógicos (`and`, `or`, `not`).
- `clase2_if_simple.py`: Ejemplo básico de la sentencia `if`.
- `clase2_if_else.py`: Ejemplo de la sentencia `if-else` (mayoría de edad).
- `clase2_if_elif_else.py`: Ejemplo de `if-elif-else` (clasificar número).
- `clase2_practica.py`: Soluciones a los ejercicios prácticos realizados en clase (Mayoría de edad, Calificación de Notas, Login Simple).

## Tareas / Ejercicios Propuestos

1.  **Validación de Nota:** Modifica el script `clase2_practica.py` (Ejercicio 2: Calificación de Notas). Añade una comprobación inicial para verificar si la nota introducida por el usuario está realmente dentro del rango válido [0, 100]. Si no lo está, muestra un mensaje de "Nota inválida" y no intentes clasificarla. Si la nota es válida, procede con la clasificación usando `if-elif-else` como antes.
2.  **Feedback de Login Mejorado:** Modifica el script `clase2_practica.py` (Ejercicio 3: Login Simple). En lugar de solo decir "Credenciales incorrectas", intenta dar mensajes más específicos:
    - Si el usuario es incorrecto, muestra "Usuario no encontrado."
    - Si el usuario es correcto PERO la contraseña es incorrecta, muestra "Contraseña incorrecta."
    - Si ambos son correctos, muestra "Acceso concedido."
    - _Pista:_ Probablemente necesitarás usar `if-elif-else` o `if` anidados.
3.  **Calculadora con Menú:** Crea un script que:
    - Muestre un menú simple al usuario: "1. Sumar", "2. Restar", "3. Multiplicar", "4. Dividir".
    - Pida al usuario que elija una opción (1-4).
    - Pida al usuario dos números.
    - Según la opción elegida, realice la operación correspondiente y muestre el resultado.
    - Si el usuario elige una opción inválida, muestre un mensaje de error.
    - _Pista:_ Necesitarás `if-elif-else` para manejar la opción elegida. ¡Cuidado con la división por cero!

_(Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_02/`)_
