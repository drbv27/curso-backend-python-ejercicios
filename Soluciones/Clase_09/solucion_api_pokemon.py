# Soluciones/Clase_09/solucion_api_pokemon.py
import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def obtener_info_pokemon(nombre_pokemon):
    """
    Obtiene y muestra información de un Pokémon desde la PokéAPI.
    """
    # Convertimos el nombre a minúsculas y quitamos espacios
    nombre_limpio = nombre_pokemon.lower().strip()
    if not nombre_limpio:
        print("❌ Error: El nombre del Pokémon no puede estar vacío.")
        return

    url_completa = BASE_URL + nombre_limpio
    print(f"\nBuscando información de '{nombre_limpio}' en {url_completa}...")

    try:
        response = requests.get(url_completa, timeout=10)
        # Lanzará una excepción para códigos 4xx/5xx (ej: 404 Not Found)
        response.raise_for_status()

        # Convertimos la respuesta JSON a un diccionario Python
        datos = response.json()

        # Extraemos e imprimimos la información que nos interesa
        print("\n---  Pokédex Info ---")
        print(f"Nombre: {datos['name'].capitalize()}")
        print(f"ID Nacional: {datos['id']}")
        print(f"Altura: {datos['height'] / 10} m") # La API da la altura en decímetros
        print(f"Peso: {datos['weight'] / 10} kg") # La API da el peso en hectogramos

        # Extraemos los tipos
        tipos = [tipo['type']['name'].capitalize() for tipo in datos['types']]
        print(f"Tipo(s): {', '.join(tipos)}")

        # Extraemos una habilidad
        if datos['abilities']:
            primera_habilidad = datos['abilities'][0]['ability']['name'].capitalize()
            print(f"Una habilidad: {primera_habilidad}")
        print("--------------------\n")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"❌ Error: Pokémon '{nombre_limpio}' no encontrado.")
        else:
            print(f"❌ Error HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Ocurrió un error de red: {req_err}")

if __name__ == "__main__":
    while True:
        pokemon_a_buscar = input("Introduce el nombre de un Pokémon (o 'salir' para terminar): ")
        if pokemon_a_buscar.lower() == 'salir':
            break
        obtener_info_pokemon(pokemon_a_buscar)