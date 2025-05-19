# archivo: clase6_funciones.py

print("--- Definición y Llamada Simple ---")
def mi_primera_funcion():
    print("¡Bienvenido/a desde mi_primera_funcion!")
    print("Este código se ejecutará cada vez que la llame.")

def funcion_que_no_hace_nada_aun():
    pass # 'pass' es una instrucción que no hace nada.

mi_primera_funcion()
funcion_que_no_hace_nada_aun()
print("-" * 20)


print("--- Parámetros y Argumentos Posicionales ---")
def saludar_persona(nombre_param): # 'nombre_param' es un parámetro
    print(f"¡Qué tal, {nombre_param}!")

saludar_persona("Valentina") # "Valentina" es el argumento para nombre_param
saludar_persona("David")
print("-" * 20)


def suma_sencilla(a, b): # 'a' y 'b' son parámetros
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

suma_sencilla(5, 10)
# suma_sencilla(5) # TypeError: suma_sencilla() missing 1 required positional argument: 'b'
print("-" * 20)


print("--- Argumentos Nombrados (Keyword Arguments) ---")
suma_sencilla(a=7, b=3)
suma_sencilla(b=20, a=15) # El orden no importa si los nombramos

def describir_item(nombre, cantidad, precio_unitario):
    print(f"Item: {nombre}, Cantidad: {cantidad}, Precio/unidad: ${precio_unitario:.2f}")

describir_item("Manzanas", 5, precio_unitario=0.50)
describir_item(cantidad=3, nombre="Peras", precio_unitario=0.75)
# describir_item(precio_unitario=1.25, "Bananos", 12) # SyntaxError: positional argument follows keyword argument
print("-" * 20)