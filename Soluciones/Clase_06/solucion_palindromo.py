# Solución Tarea Clase 6: Verificador de Palíndromos

def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo.
    Un palíndromo se lee igual al derecho y al revés.
    Ignora mayúsculas/minúsculas y espacios al principio/final.

    Args:
        palabra (str): La palabra a verificar.

    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """
    if not isinstance(palabra, str):
        return False # O podrías lanzar un error o un mensaje

    # Procesamiento: minúsculas y sin espacios al inicio/final
    palabra_procesada = palabra.lower().strip()

    # Si la palabra procesada está vacía, podría considerarse palíndromo
    # o no, según la definición. Aquí la consideraremos no palíndromo
    # para evitar que un string vacío sea palíndromo por defecto.
    if not palabra_procesada:
        return False

    palabra_invertida = palabra_procesada[::-1] # Slicing para invertir

    return palabra_procesada == palabra_invertida

print("--- Verificador de Palíndromos ---")
palabras_test = ["Ana", "Radar", "Reconocer", "Somos", "Python", "Hola", " ", "Luz azul"]

for p in palabras_test:
    if es_palindromo(p):
        print(f"'{p}' SÍ es un palíndromo.")
    else:
        print(f"'{p}' NO es un palíndromo.")

# Ejemplo con input del usuario
palabra_usuario = input("\nIntroduce una palabra para verificar si es palíndromo: ")
if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' SÍ es un palíndromo.")
else:
    print(f"'{palabra_usuario}' NO es un palíndromo.")
print("-" * 20)