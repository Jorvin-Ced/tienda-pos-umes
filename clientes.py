def registrar_cliente(lista_clientes):
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    nit = input("Ingrese el NIT del cliente (o 'CF'): ").strip().upper()
    
    # Validación: Si es CF no importa si se repite, pero si es un NIT específico
    # debemos revisar que no exista ya en la base de datos de Doña Marta.
    if nit != "CF":
        for cliente in lista_clientes:
            if cliente["nit"] == nit:
                print(f"¡Error! El cliente con NIT {nit} ya se encuentra registrado.")
                print(f"Nombre registrado: {cliente['nombre']}")
                return

    nombre = input("Nombre completo del cliente: ").strip()
    telefono = input("Teléfono de contacto: ").strip()
    
    # Estructura de diccionario exigida para el JSON
    nuevo_cliente = {
        "nit": nit,
        "nombre": nombre,
        "telefono": telefono
    }
    
    lista_clientes.append(nuevo_cliente)
    print(f"¡Cliente '{nombre}' registrado exitosamente!")

def mostrar_clientes(lista_clientes):
    print("\n--- BASE DE DATOS DE CLIENTES ---")
    if not lista_clientes:
        print("No hay clientes registrados aún.")
        return
        
    print(f"{'NIT':<15} | {'Nombre':<25} | {'Teléfono':<12}")
    print("-" * 58)
    for cliente in lista_clientes:
        print(f"{cliente['nit']:<15} | {cliente['nombre']:<25} | {cliente['telefono']:<12}")

def menu_clientes(lista_clientes):
    """Función principal que conecta con main.py"""
    while True:
        print("\n=== MENÚ DE CLIENTES ===")
        print("1. Registrar Cliente")
        print("2. Mostrar Lista de Clientes")
        print("3. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente(lista_clientes)
        elif opcion == "2":
            mostrar_clientes(lista_clientes)
        elif opcion == "3":
            print("Regresando...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")