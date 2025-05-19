# Solución Tarea Clase 5: Contador de Frecuencia de Palabras

def contar_frecuencia_palabras(texto):
    frecuencias = {}
    if not texto.strip(): # Si el texto está vacío o solo espacios
        return frecuencias

    # Convertir a minúsculas y eliminar puntuación básica (simple)
    # Para un análisis más robusto se necesitarían expresiones regulares
    texto_limpio = texto.lower()
    caracteres_a_eliminar = ",.;:!?\"'()"
    for char in caracteres_a_eliminar:
        texto_limpio = texto_limpio.replace(char, "")

    palabras = texto_limpio.split() # Divide el string en una lista de palabras

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

print("--- Contador de Frecuencia de Palabras ---")
frase_ejemplo = "Hola mundo, este es un mundo maravilloso y hola otra vez mundo."
print(f"Frase original: \"{frase_ejemplo}\"")

frecuencia_palabras = contar_frecuencia_palabras(frase_ejemplo)

if frecuencia_palabras:
    print("\nFrecuencia de cada palabra:")
    for palabra, conteo in frecuencia_palabras.items():
        print(f"- '{palabra}': {conteo}")
else:
    print("No se encontraron palabras en el texto.")

print("-" * 20)

frase_vacia = "   "
print(f"Frase vacía: \"{frase_vacia}\"")
frecuencia_vacia = contar_frecuencia_palabras(frase_vacia)
print(f"Frecuencia: {frecuencia_vacia}")
print("-" * 20)