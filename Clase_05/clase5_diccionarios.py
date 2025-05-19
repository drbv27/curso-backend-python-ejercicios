# archivo: clase5_diccionarios.py

print("--- Creando Diccionarios ---")
persona = {
    "nombre": "Carlos",
    "edad": 32,
    "ciudad": "Medellín",
    "hobbies": ["programar", "leer", "senderismo"]
}
print(f"Persona: {persona}")

configuracion = dict(host="localhost", puerto=5432, db_nombre="mi_base_datos")
print(f"Configuración: {configuracion}")

diccionario_vacio = {}
print(f"Diccionario vacío: {diccionario_vacio}, tipo: {type(diccionario_vacio)}")
print("-" * 20)


print("--- Accediendo a Valores ---")
print(f"Nombre de la persona: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Primer hobby: {persona['hobbies'][0]}")

# Acceso seguro con get()
profesion = persona.get("profesion")
print(f"Profesión (con get, no existe): {profesion}")
profesion_default = persona.get("profesion", "No especificada")
print(f"Profesión (con get y default): {profesion_default}")
print("-" * 20)


print("--- Añadir y Modificar Pares ---")
persona["edad"] = 33 # Modificar
print(f"Edad actualizada: {persona['edad']}")
persona["profesion"] = "Desarrollador Backend" # Añadir
persona["email"] = "carlos.dev@example.com"  # Añadir
print(f"Persona con nuevos datos: {persona}")
print("-" * 20)


print("--- Eliminar Pares ---")
if "email" in persona:
    email_eliminado = persona.pop("email")
    print(f"Email eliminado: {email_eliminado}")
pais = persona.pop("pais", "No encontrado") # No existe, usa default
print(f"Intentando pop('pais'): {pais}")

if "hobbies" in persona:
    del persona["hobbies"]
    print(f"Persona después de del['hobbies']: {persona}")

if persona: # Si no está vacío
    ultimo_par = persona.popitem()
    print(f"Par eliminado con popitem(): {ultimo_par}")
print(f"Persona al final: {persona}")
print("-" * 20)


print("--- Verificar Existencia de Claves ---")
persona_actual = {"nombre": "Ana", "edad": 28}
print(f"'edad' in persona_actual? {'edad' in persona_actual}")
print(f"'ciudad' not in persona_actual? {'ciudad' not in persona_actual}")
print("-" * 20)


print("--- Vistas del Diccionario ---")
config = {"host": "mi.servidor.com", "port": 80, "timeout": 30}
print(f"Diccionario config: {config}")
print(f"Claves: {config.keys()}")
print(f"Valores: {config.values()}")
print(f"Items: {config.items()}")
print("-" * 20)


print("--- Iterando sobre Diccionarios ---")
print("Iterando sobre claves (y accediendo a valor):")
for k in config:
    print(f"Clave: {k}, Valor: {config[k]}")

print("\nIterando sobre ítems (clave, valor):")
for clave_actual, valor_actual in config.items():
    print(f"'{clave_actual}' tiene asignado '{valor_actual}'")
print("-" * 20)

print(f"Número de elementos en config: {len(config)}")