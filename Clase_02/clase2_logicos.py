edad = 22
tiene_carnet = True
saldo_cuenta = 50
es_vip = False
esta_trabajando = False

# Ejemplo con 'and'
puede_conducir_coche = edad >= 18 and tiene_carnet == True
print(f"¿Puede conducir coche? {puede_conducir_coche}")

# Ejemplo con 'or'
tiene_acceso_preferente = saldo_cuenta > 1000 or es_vip == True
print(f"¿Tiene acceso preferente? {tiene_acceso_preferente}")

# Ejemplo con 'not'
puede_salir = not esta_trabajando
print(f"¿Puede salir? {puede_salir}")

# Ejemplo combinado con paréntesis
# ¿Es mayor de edad Y (tiene carnet O es vip)?
condicion_compleja = edad >= 18 and (tiene_carnet or es_vip)
print(f"Condición compleja (edad>=18 and (carnet or vip)): {condicion_compleja}")