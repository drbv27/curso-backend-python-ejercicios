# Clase_09/clase9_practica_requests.py
import requests
import json # Para imprimir el JSON de forma bonita

# URL de una API pública de prueba (nos da un "to-do" falso)
# Vamos a pedir el to-do con ID 5
url = "https://jsonplaceholder.typicode.com/todos/5"

print(f"Haciendo petición GET a: {url}")

try:
    # Realizamos la petición GET con un timeout de 5 segundos
    response = requests.get(url, timeout=5)

    # raise_for_status() lanzará una excepción si el código de estado es de error (4xx o 5xx)
    response.raise_for_status()

    # --- Si llegamos aquí, la petición fue exitosa (código 2xx) ---

    print(f"\n✅ Petición exitosa! Código de Estado: {response.status_code}")

    # Inspeccionamos algunas cabeceras de la respuesta
    print("\n--- Cabeceras de la Respuesta (algunas) ---")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"Date: {response.headers.get('Date')}")
    print("-" * 20)

    # Inspeccionamos el cuerpo de la respuesta
    # .text lo devuelve como un string
    print("\n--- Cuerpo de la Respuesta (formato texto) ---")
    print(response.text)
    print("-" * 20)

    # .json() lo convierte automáticamente a un diccionario o lista Python
    print("\n--- Cuerpo de la Respuesta (interpretado como JSON) ---")
    datos = response.json()

    # Usamos json.dumps para imprimir el diccionario de forma legible
    print(json.dumps(datos, indent=4))
    print("-" * 20)

    # Ahora podemos trabajar con 'datos' como un diccionario normal
    print("\n--- Accediendo a los datos del diccionario Python ---")
    print(f"ID de Usuario: {datos.get('userId')}")
    print(f"Título de la tarea: '{datos.get('title')}'")
    if datos.get('completed'):
        print("Estado: Completada")
    else:
        print("Estado: Pendiente")
    print("-" * 20)

except requests.exceptions.HTTPError as http_err:
    print(f"❌ Error HTTP: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"❌ Error de Conexión: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"❌ Error de Timeout: La petición tardó demasiado en responder. {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"❌ Ocurrió un error en la petición: {req_err}")