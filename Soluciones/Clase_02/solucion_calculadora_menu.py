# Solución Tarea Clase 2: Calculadora con Menú

print("--- Calculadora Simple con Menú ---")
print("Opciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion_str = input("Elige una opción (1-4): ")

try:
    opcion = int(opcion_str)

    # Validamos la opción elegida
    if opcion >= 1 and opcion <= 4:
        # Pedimos los números SOLO si la opción es válida
        num1_str = input("Introduce el primer número: ")
        num2_str = input("Introduce el segundo número: ")
        num1 = float(num1_str)
        num2 = float(num2_str)

        resultado = None # Inicializamos resultado

        # Realizamos la operación según la opción
        if opcion == 1:
            resultado = num1 + num2
            operador = "+"
        elif opcion == 2:
            resultado = num1 - num2
            operador = "-"
        elif opcion == 3:
            resultado = num1 * num2
            operador = "*"
        elif opcion == 4:
            # Verificación de división por cero
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
                operador = "/"
                resultado = "Indefinido"
            else:
                resultado = num1 / num2
                operador = "/"

        # Mostramos el resultado si no hubo error de división por cero
        if resultado != "Indefinido":
             print(f"Resultado: {num1} {operador} {num2} = {resultado}")

    else:
        print("Error: Opción inválida. Debes elegir entre 1 y 4.")

except ValueError:
    print("Error: Entrada inválida. La opción y los números deben ser valores numéricos.")

print("-" * 20)