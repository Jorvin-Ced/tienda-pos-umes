# 1. Importaiones correctas, no pendejo, no es necesario importar todo el modulo, solo lo que se va a usar
import productos
import clientes
import ventas
import reportes
import utilidades

def main():
    # 2. Esto ya aqui se carga la base de datos pa que entendas 
    BD_PRODUCTOS = utilidades.cargar_datos("productos.json")
    BD_CLIENTES = utilidades.cargar_datos("clientes.json")
    BD_VENTAS = utilidades.cargar_datos("ventas.json")

    # 3. no pendejo, este es el menu, osea el inicio 
    while True:
        print("=================================")
        print("   SISTEMA POS - TU TIENDA       ")
        print("=================================")
        print("1. Módulo de Productos")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas (Caja)")
        print("4. Módulo de Reportes")
        print("5. Salir del Sistema")
        
        try:
            opcion = input("Seleccione una opción (1-5): ")
            
            # aqui corrige las lineas pendejo >:v
            if opcion == "1":
                productos.menu_productos(BD_PRODUCTOS)
                utilidades.guardar_datos("productos.json", BD_PRODUCTOS)
                
            elif opcion == "2":
                clientes.menu_clientes(BD_CLIENTES)
                utilidades.guardar_datos("clientes.json", BD_CLIENTES)
                
            elif opcion == "3":
                ventas.menu_ventas(BD_VENTAS, BD_PRODUCTOS, BD_CLIENTES)
                utilidades.guardar_datos("ventas.json", BD_VENTAS)
                utilidades.guardar_datos("productos.json", BD_PRODUCTOS)
                
            elif opcion == "4":
                reportes.menu_reportes(BD_VENTAS, BD_PRODUCTOS)
                
            elif opcion == "5":
                print("Cerrando sistema de forma segura. ¡Feliz día Doña Marta!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                
        except Exception as e:
            print(f"Ocurrió un error inesperado en el menú principal: {e}")

if __name__ == "__main__":
    main()