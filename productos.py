def registrar_producto(lista_productos):
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    try:
        codigo = input("Ingrese el código único del producto: ").strip().upper()
        
        for prod in lista_productos:
            if prod["codigo"] == codigo:
                print("¡Error! Este código ya existe en el inventario.")
                return

        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría (Abarrotes, Bebidas, etc.): ").strip()
        precio = float(input("Precio de venta (en Q): "))
        stock = int(input("Cantidad inicial en stock: "))
        stock_minimo = int(input("Stock mínimo de alerta: "))
        
        if precio < 0 or stock < 0 or stock_minimo < 0:
            print("Error: Los valores numéricos no pueden ser negativos.")
            return
        
        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "stock_minimo": stock_minimo
        }
        
        lista_productos.append(nuevo_producto)
        print(f"¡Producto '{nombre}' registrado exitosamente!")
        
    except ValueError:
        print("Error: El precio y el stock deben ser valores numéricos.")

def mostrar_inventario(lista_productos):
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    if not lista_productos:
        print("El inventario está vacío.")
        return
        
    print(f"{'Código':<10} | {'Nombre':<20} | {'Categoría':<15} | {'Precio':<8} | {'Stock':<6}")
    print("-" * 70)
    for prod in lista_productos:
        print(f"{prod['codigo']:<10} | {prod['nombre']:<20} | {prod['categoria']:<15} | Q{prod['precio']:<7.2f} | {prod['stock']:<6}")

def buscar_producto(lista_productos):
    print("\n--- BUSCAR PRODUCTO ---")
    busqueda = input("Ingrese el código o nombre a buscar: ").strip().lower()
    encontrados = []
    
    for prod in lista_productos:
        if busqueda in prod["codigo"].lower() or busqueda in prod["nombre"].lower():
            encontrados.append(prod)
            
    if not encontrados:
        print("No se encontraron productos que coincidan.")
    else:
        mostrar_inventario(encontrados)

def menu_productos(lista_productos):
    while True:
        print("\n=== MENÚ DE PRODUCTOS ===")
        print("1. Registrar Producto")
        print("2. Mostrar Inventario")
        print("3. Buscar Producto (Parcial)")
        print("4. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(lista_productos)
        elif opcion == "2":
            mostrar_inventario(lista_productos)
        elif opcion == "3":
            buscar_producto(lista_productos)
        elif opcion == "4":
            print("Regresando...")
            break
        else:
            print("Opción inválida.")