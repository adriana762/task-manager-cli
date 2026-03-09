
"""
    main
"""
from storage import load_task
from task_service import create_task, complete_task, delete_task, show_task

data_task = load_task()

while True:
    print("\n 1- Crear tarea.")
    print("\n 2- Completar tarea.")
    print("\n 3- Eliminar tarea.")
    print("\n 4- Ver tarea.")
    print("\n 5- Salir.")

    option = input ("Elegi una opcion:")
    if option == '1':
        titulo = input("Titulo de la tarea: ")
        create_task(data_task, titulo)
    elif option == '2':
        ID = input("ID de la tarea a completar: ")
        complete_task(data_task, ID)
    elif option == '3':
        ID = input("ID de la tarea a eliminar: ")
        delete_task(data_task, ID)
    elif option == '4':
        print("\n 1- Todas las tareas.")
        print("\n 2- Tareas hechas.")
        print("\n 3- Tareas pendientes.")
        filter_option = input("Elegi una opcion.")
        show_task(data_task, filter_option)
    elif option == '5':
        break