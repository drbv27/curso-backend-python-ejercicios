# archivo: clase6_scope.py

variable_global_curso = "Python Backend" # Variable Global
print(f"NIVEL GLOBAL (antes de funciones) - variable_global_curso: {variable_global_curso}")

def funcion_con_scope():
    variable_local_funcion = "Soy local de esta función" # Variable Local
    print(f"  Dentro de funcion_con_scope - Local: {variable_local_funcion}")
    print(f"  Dentro de funcion_con_scope - Global (leída): {variable_global_curso}")

    # Si descomentas la siguiente línea, creas una variable local 'variable_global_curso'
    # que "sombrea" (oculta) la global DENTRO de esta función.
    # variable_global_curso = "Modificada localmente por funcion_con_scope"
    # print(f"  Dentro de funcion_con_scope - 'Global' sombreada: {variable_global_curso}")

def otra_funcion():
    # print(variable_local_funcion) # NameError: variable_local_funcion no está definida aquí
    print(f"  En otra_funcion - Global (leída): {variable_global_curso}")

def intentar_modificar_global_sin_keyword():
    # Esto crea una NUEVA variable LOCAL con el mismo nombre.
    # NO modifica la variable_global_curso original.
    variable_global_curso = "Nuevo valor local"
    print(f"  Dentro de intentar_modificar_global_sin_keyword (LOCAL): {variable_global_curso}")


def modificar_global_con_keyword():
    global variable_global_curso # Avisamos que vamos a usar la global
    variable_global_curso = "Python Backend Avanzado con global"
    print(f"  Dentro de modificar_global_con_keyword (GLOBAL MODIFICADA): {variable_global_curso}")


print("\nLlamando a funcion_con_scope():")
funcion_con_scope()

print("\nLlamando a otra_funcion():")
otra_funcion()

print(f"\nNIVEL GLOBAL (después de scope y otra_funcion) - variable_global_curso: {variable_global_curso}")

print("\nLlamando a intentar_modificar_global_sin_keyword():")
intentar_modificar_global_sin_keyword()
print(f"NIVEL GLOBAL (después de intentar_mod_sin_keyword) - variable_global_curso: {variable_global_curso}") # Sigue igual

print("\nLlamando a modificar_global_con_keyword():")
modificar_global_con_keyword()
print(f"NIVEL GLOBAL (después de modificar_con_keyword) - variable_global_curso: {variable_global_curso}") # ¡Cambió!