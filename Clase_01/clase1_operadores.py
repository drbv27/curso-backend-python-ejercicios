# Operadores Aritméticos
print("--- Operadores Aritméticos ---")
num1 = 15
num2 = 4

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
potencia = num2 ** 2  # 4 elevado a la 2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}") # División siempre float
print(f"{num1} // {num2} = {division_entera}")
print(f"{num1} % {num2} = {modulo}")
print(f"{num2} ** 2 = {potencia}")

# Operadores de Asignación
print("\n--- Operadores de Asignación ---")
contador = 10
print(f"Contador inicial: {contador}")
contador += 5  # contador = contador + 5
print(f"Después de += 5: {contador}")
contador *= 3  # contador = contador * 3
print(f"Después de *= 3: {contador}")
contador //= 4 # contador = contador // 4
print(f"Después de //= 4: {contador}")