"""
    funciones
"""
import random
from storage import dump_task

def task_done(data_task):
    """Mostrar tareas hechas"""
    i = 1
    done = False
    for tarea in data_task:
        if tarea['completed'] is True:
            done = True
            print(f"{i}- [{tarea['id']}] {tarea['title']} - <<<DONE>>>")
            i += 1
    if done is False:
        print("No hay tareas hechas")
def task_pending(data_task):
    """Mostrar tareas pendientes"""
    pending = False
    i = 1
    for tarea in data_task:
        if tarea['completed'] is False:
            pending = True
            print(f"{i}- [{tarea['id']}] {tarea['title']} - <<<PENDING>>>")
            i += 1
    if pending is False:
        print("No hay tareas pendientes")

def show_task(data_task, opc):
    """
    imprimo tareas
    opc = 1 --> muestra todas las tareas
    opc = 2 --> muestra las tareas hechas
    opc = 3 --> muestra las tareas pendientes
    """
    i = 1
    if not data_task:
        print("No hay tareas.")
        return
    if opc == '1':
        for tarea in data_task:
            if tarea['completed'] is True:
                estado = '<<<DONE>>>'
            else:
                estado = '<<<PENDING>>>'
            print(f"{i}- [{tarea['id']}] {tarea['title']} - {estado}")
            i += 1
    elif opc == '2':
        task_done(data_task)
    elif opc == '3':
        task_pending(data_task)

def create_task(data_task, title):
    """
    Genero ID's y guardo datos
    """
    dict_task = {} #diccionario
    i = 0
    #generar un ID automaticamente
    longitud = 8
    repetido = True
    while repetido:
        i = 0
        repetido = False
        id_ = random.randint(0, 99999999)

        while i < len(data_task):
            if data_task[i]['id'] == str(id_).zfill(longitud):
                repetido = True
                break
            i += 1
    #guardar la terea en la lista
    dict_task['id'] = str(id_).zfill(longitud)
    dict_task['title'] = title
    dict_task['completed'] = False
    data_task.append(dict_task)
    #guardar los datos en el archivo json
    dump_task(data_task)

def complete_task(data_task, task_id):
    """
    buscar la tarea, si la encuentra cambia el flag en la lista y el archivo
    """
    encontrado = False
    for find_dict in data_task:
        if find_dict['id'] == task_id:
            find_dict['completed'] = True
            encontrado = True
    if not encontrado:
        print(f"Tarea{task_id} no encontrada.")
    dump_task(data_task)

def delete_task(data_task, task_id):
    """
    Elimino tarea
    """
    for find_tarea in data_task:
        #elimino tarea de la lista
        if find_tarea['id'] == task_id:
            data_task.remove(find_tarea)
            break
    #elimino tarea del archivo (data_task esta modificado)
    dump_task(data_task)