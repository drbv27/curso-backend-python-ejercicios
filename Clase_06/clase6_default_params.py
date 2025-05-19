# archivo: clase6_default_params.py

def generar_saludo_completo(nombre, saludo_base="Hola", puntuacion="!"):
    """Genera un saludo completo con opciones por defecto."""
    return f"{saludo_base}, {nombre}{puntuacion}"

print(generar_saludo_completo("Juan"))
print(generar_saludo_completo("Maria", saludo_base="Buenos días"))
print(generar_saludo_completo("Pedro", puntuacion="!!!"))
print(generar_saludo_completo("Ana", "Hey", "??"))
print(generar_saludo_completo("Luis", puntuacion=".", saludo_base="Qué tal"))
print(generar_saludo_completo(nombre="Elena", saludo_base="Saludos"))


def crear_configuracion(host, puerto=80, protocolo="http"):
    """Crea una URL de configuración."""
    return f"{protocolo}://{host}:{puerto}"

print(crear_configuracion("miapi.com"))
print(crear_configuracion("miapi.com", puerto=443, protocolo="https"))
print(crear_configuracion("localhost", protocolo="ws", puerto=9000))