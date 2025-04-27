temperatura_actual = 15
# Prueba cambiando este valor a 30 y vuelve a ejecutar

print("Evaluando la temperatura...")

# La condición es temperatura_actual < 20
if temperatura_actual < 20:
    # Este bloque SÓLO se ejecuta si la condición es True
    print("Hace fresco.")
    print("Deberías llevar una chaqueta.")
    print("Fin del bloque if.")

# Esta línea NO está indentada respecto al if, por lo que está fuera.
# Se ejecuta siempre.
print(f"La temperatura reportada es: {temperatura_actual}°C")