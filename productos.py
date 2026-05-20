def registrar_producto(lista_productos):
    print("--- REGISTRAR NUEVO PRODUCTO ---")
    try:
        codigo = input("Ingrese el código único del producto: ").strip()
        
        for prod in lista_productos:
            if prod["codigo"] == codigo:
                print("¡Error! Este código ya existe en el inventario.")
                return

        nombre = input("Nombre del producto: ").strip()
        precio = float(input("Precio de venta (en Q): "))
        stock = int(input("Cantidad inicial en stock: "))
        
        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }
        
        lista_productos.append(nuevo_producto)
        print(f"¡Producto '{nombre}' registrado exitosamente!")
        
    except ValueError:
        print("Error: El precio y el stock deben ser valores numéricos.")

def mostrar_inventario(lista_productos):
    print("--- INVENTARIO DE PRODUCTOS ---")
    if not lista_productos:
        print("El inventario está vacío.")
        return
        
    print(f"{'Código':<12} | {'Nombre':<20} | {'Precio':<10} | {'Stock':<6}")
    print("-" * 55)
    for prod in lista_productos:
        print(f"{prod['codigo']:<12} | {prod['nombre']:<20} | Q{prod['precio']:<9.2f} | {prod['stock']:<6}")

def menu_productos(lista_productos):
    while True:
        print("=== MENÚ DE PRODUCTOS ===")
        print("1. Registrar Producto")
        print("2. Mostrar Inventario")
        print("3. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(lista_productos)
        elif opcion == "2":
            mostrar_inventario(lista_productos)
        elif opcion == "3":
            print("Regresando...")
            break
        else:
            print("Opción inválida.")
            # aqui va la logica, no seas pendejo xD