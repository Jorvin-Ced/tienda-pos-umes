import json
import os

def cargar_datos(nombre_archivo):
    """Carga un archivo JSON. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(nombre_archivo):
        return [] # Retorna lista vacía para que no colapse el sistema
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print(f"Error al leer {nombre_archivo}. Archivo corrupto. Se inicializará vacío.")
        return []

def guardar_datos(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON de forma inmediata."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error crítico al guardar en {nombre_archivo}: {e}")