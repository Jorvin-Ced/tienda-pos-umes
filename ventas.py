import datetime
import os

def buscar_cliente(nit, lista_clientes):
    # Si el NIT es CF, devolvemos un diccionario con datos generéricos
    if nit == "CF":
        return {"nit": "CF", "nombre": "Consumidor Final", "telefono": "-", "email": "-"}
    
    # Recorremos la lista de clientes uno por uno buscando el NIT
    for cliente in lista_clientes:
        if cliente["nit"] == nit:
            return cliente # Si lo encuentra, devuelve al cliente
            
    return None # Si no lo encuentra, devuelve Nada

def mostrar_carrito(carrito):
    print("--- CARRITO DE COMPRAS ---")
    
    # Si el carrito no tiene elementos, mostramos mensaje y devolvemos total 0
    if len(carrito) == 0:
        print("El carrito está vacío.")
        return 0
        
    total_acumulado = 0
    print("Producto             | Cantidad | Precio U. | Subtotal")
    print("-------------------------------------------------------")
    
    # Recorremos cada producto agregado al carrito para imprimirlo
    for item in carrito:
        print(f"{item['nombre']:<20} | {item['cantidad']:<8} | Q{item['precio_unit']:<8.2f} | Q{item['subtotal']:<8.2f}")
        total_acumulado = total_acumulado + item["subtotal"]
        
    return total_acumulado # Devolvemos la suma de toda la venta

def generar_factura_txt(id_venta, fecha, cliente, carrito, subtotal, iva, total):
    # Si la carpeta 'facturas' no existe en la computadora, Python la crea sola
    if not os.path.exists("facturas"):
        os.makedirs("facturas")
        
    # Definimos la ruta y nombre del archivo de texto
    nombre_archivo = "facturas/factura_" + id_venta + ".txt"
    
    # Abrimos el archivo para escribir la información de la factura
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("=========================================")
        f.write("          SISTEMA POS - TU TIENDA        ")
        f.write("=========================================")
        f.write("Factura No: " + str(id_venta) + "\n")
        f.write("Fecha: " + str(fecha) + "\n")
        f.write("NIT Cliente: " + str(cliente["nit"]) + "\n")
        f.write("Nombre: " + str(cliente["nombre"]) + "\n")
        f.write("-----------------------------------------")
        f.write("Producto             | Cant. | Total     ")
        f.write("-----------------------------------------")
        for item in carrito:
            f.write(f"{item['nombre']:<20} | {item['cantidad']:<5} | Q{item['subtotal']:<8.2f}\n")
        f.write("-----------------------------------------\n")
        f.write(f"Subtotal:  Q{subtotal:.2f}\n")
        f.write(f"IVA (12%): Q{iva:.2f}\n")
        f.write(f"TOTAL:     Q{total:.2f}\n")
        f.write("=========================================\n")

def menu_ventas(lista_ventas, lista_productos, lista_clientes):
    print("")
    print("--- INICIAR NUEVA VENTA ---")
    nit = input("Ingrese el NIT del cliente (o 'CF'): ").strip().upper()
    
    # Buscamos si el cliente existe usando la función de arriba (con validación limpia)
    cliente = buscar_cliente(nit, lista_clientes)
    
    # Si el cliente no existe y tampoco es CF, comio mierda xD se detiene la venta
    if cliente is None:
        print("¡Error! El cliente no está registrado.")
        print("Regístrelo primero en el Módulo de Clientes.")
        return

    print("Cliente seleccionado: " + cliente["nombre"])
    
    # Creamos una lista vacía para almacenar los productos de ESTA venta
    carrito = [] 
    
    # Bucle secundario para controlar las opciones de la venta en curso
    while True:
        print("")
        print("=== CAJA / OPCIONES DE VENTA ===")
        print("1. Agregar Producto al Carrito")
        print("2. Mostrar Carrito Actual")
        print("3. Confirmar y Facturar Venta")
        print("4. Cancelar Venta")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("")
            codigo = input("Ingrese el código del producto: ").strip().upper()
            
            # aqui se busca el producto
            producto_encontrado = None
            for p in lista_productos:
                if p["codigo"] == codigo:
                    producto_encontrado = p
                    break
            
            if producto_encontrado is None:
                print("¡Error! Producto no encontrado.")
            else:
                try:
                    cantidad = int(input("Cantidad a llevar de " + producto_encontrado["nombre"] + ": "))
                    if cantidad <= 0:
                        print("Error: La cantidad debe ser mayor a 0.")
                        continue
                    
                    # Validacion de stock en tienda kbron
                    if producto_encontrado["stock"] < cantidad:
                        print("¡Error! No hay suficiente stock. Solo quedan: " + str(producto_encontrado["stock"]))
                    else:
                        # Creamos un diccionario simple para el artículo comprado
                        articulo = {
                            "codigo": codigo,
                            "nombre": producto_encontrado["nombre"],
                            "cantidad": cantidad,
                            "precio_unit": producto_encontrado["precio"],
                            "subtotal": cantidad * producto_encontrado["precio"]
                        }
                        # Lo metemos al carrito temporal
                        carrito.append(articulo)
                        print("¡Producto agregado al carrito con éxito!")
                except ValueError:
                    print("Error: Ingrese un número entero válido.")
                    
        elif opcion == "2":
            print("")
            mostrar_carrito(carrito)
            
        elif opcion == "3":
            print("")
            total_venta = mostrar_carrito(carrito)
            if total_venta == 0:
                print("No puede facturar una venta vacía.")
                continue
                
            confirmar = input("¿Desea confirmar y cobrar la venta? (S/N): ").strip().upper()
            if confirmar == "S":
                # Calculamos el IVA (12%) y el subtotal según leyes de Guatemala
                iva_calculado = total_venta * 0.12
                subtotal_calculado = total_venta - iva_calculado
                
                # Descontamos el stock de la lista de productos real
                for item in carrito:
                    for p in lista_productos:
                        if p["codigo"] == item["codigo"]:
                            p["stock"] = p["stock"] - item["cantidad"]
                            break
                
                # Generamos un ID automático para la venta (Ej: V1, V2...)
                id_generado = "V" + str(len(lista_ventas) + 1)
                fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Creamos el registro de la venta final
                registro_venta = {
                    "id_venta": id_generado,
                    "fecha": fecha_hoy,
                    "nit_cliente": cliente["nit"],
                    "items": carrito,
                    "subtotal": subtotal_calculado,
                    "iva": iva_calculado,
                    "total": total_venta
                }
                
                # Guardamos la venta en la base de datos principal y creamos el .txt
                lista_ventas.append(registro_venta)
                generar_factura_txt(id_generado, fecha_hoy, cliente, carrito, subtotal_calculado, iva_calculado, total_venta)
                
                print("¡Venta registrada con éxito!")
                print("Factura física creada en la carpeta 'facturas/'")
                break # Rompe el ciclo while para volver al menú de main.py
                
        elif opcion == "4":
            print("Venta cancelada. No se modificó ningún dato.")
            break
        else:
            print("Opción inválida.")