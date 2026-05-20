def registrar_cliente(lista_clientes):
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    nit = input("Ingrese el NIT del cliente (o 'CF'): ").strip().upper()
    
    if nit != "CF":
        for cliente in lista_clientes:
            if cliente["nit"] == nit:
                print(f"¡Error! El cliente con NIT {nit} ya existe.")
                return

    nombre = input("Nombre completo del cliente: ").strip()
    telefono = input("Teléfono de contacto: ").strip()
    email = input("Correo electrónico: ").strip()
    
    if nit != "CF" and ("@" not in email or "." not in email):
        print("Error: El correo electrónico no es válido (debe contener '@' y '.').")
        return
    
    nuevo_cliente = {
        "nit": nit,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    lista_clientes.append(nuevo_cliente)
    print(f"¡Cliente '{nombre}' registrado exitosamente!")

def mostrar_clientes(lista_clientes):
    print("\n--- BASE DE DATOS DE CLIENTES ---")
    if not lista_clientes:
        print("No hay clientes registrados aún.")
        return
        
    print(f"{'NIT':<12} | {'Nombre':<20} | {'Teléfono':<10} | {'Email':<20}")
    print("-" * 70)
    for cliente in lista_clientes:
        print(f"{cliente['nit']:<12} | {cliente['nombre']:<20} | {cliente['telefono']:<10} | {cliente['email']:<20}")

def menu_clientes(lista_clientes):
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
            print("Opción inválida.")