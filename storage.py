"""Manejo de archivo json"""
import json
FILE = 'data.json'
def load_task():
    """ 
    Leer el archivo 
    """
    try:
        with open(FILE, 'r', encoding = 'cp1252') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
  
def dump_task(data_task):
    """
    Guardar en archivo
    """
    with open(FILE, 'w', encoding = 'cp1252') as file:
        json.dump(data_task, file, indent = 4)