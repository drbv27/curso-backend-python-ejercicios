# Solución Tarea Clase 4: Lista de Compras Interactiva

print("--- Mi Lista de Compras Interactiva ---")
lista_compras = []

while True:
    print("\nOpciones:")
    print("1. Añadir ítem")
    print("2. Eliminar ítem")
    print("3. Ver lista")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        item_nuevo = input("¿Qué ítem deseas añadir?: ")
        lista_compras.append(item_nuevo)
        print(f"'{item_nuevo}' añadido a la lista.")
    elif opcion == "2":
        if not lista_compras: # Si la lista está vacía
            print("La lista está vacía, nada que eliminar.")
            continue
        print("Ítems actuales:", lista_compras)
        item_eliminar = input("¿Qué ítem deseas eliminar?: ")
        if item_eliminar in lista_compras:
            lista_compras.remove(item_eliminar)
            print(f"'{item_eliminar}' eliminado de la lista.")
        else:
            print(f"'{item_eliminar}' no se encontró en la lista.")
    elif opcion == "3":
        if not lista_compras:
            print("La lista de compras está vacía.")
        else:
            print("\n--- Tu Lista de Compras ---")
            for i, item in enumerate(lista_compras, 1): # enumerate para numerar
                print(f"{i}. {item}")
            print("---------------------------")
    elif opcion == "4":
        print("¡Adiós! Gracias por usar la lista de compras.")
        break
    else:
        print("Opción no válida. Por favor, elige entre 1 y 4.")