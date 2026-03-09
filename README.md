# Task Manager CLI

## 🇪🇸 Español

Pequeño gestor de tareas desarrollado en **Python** que funciona desde la **línea de comandos (CLI)**.
Este proyecto fue creado como práctica para trabajar con **modularización de código y manejo de archivos JSON como parte de mi proceso de aprendizaje**.

### Funcionalidades

* Crear nuevas tareas
* Marcar tareas como completadas
* Eliminar tareas
* Ver todas las tareas
* Filtrar tareas (completadas / pendientes)
* Persistencia de datos en archivo JSON

### Tecnologías utilizadas

* Python
* JSON para almacenamiento de datos
* Command Line Interface (CLI)
* Arquitectura modular

### Estructura del proyecto

```
task-manager-cli/
│
├── main.py          # Interfaz de usuario en la terminal
├── task_service.py  # Lógica de manejo de tareas
├── storage.py       # Lectura y escritura del archivo JSON
├── data.json        # Archivo donde se almacenan las tareas
├── .gitignore
└── README.md
```

### Cómo ejecutar el proyecto

1. Clonar el repositorio

```
git clone https://github.com/adriana762/task-manager-cli.git
```

2. Entrar al directorio del proyecto

```
cd task-manager-cli
```

3. Ejecutar el programa

```
python main.py
```

### Ejemplo de uso

```
1- Crear tarea
2- Completar tarea
3- Eliminar tarea
4- Ver tareas
5- Salir

Elegí una opcion: 1
Titulo de la tarea: Estudiar Python
```

---

## 🇬🇧 English

Small **task manager written in Python** that runs in the **command line (CLI)**.
This project was created as practice for **code modularization, JSON file handling, and basic Git/GitHub workflow**.

### Features

* Create new tasks
* Mark tasks as completed
* Delete tasks
* Show all tasks
* Filter tasks (done / pending)
* JSON file persistence

### Tech Stack

* Python
* JSON file storage
* Command Line Interface (CLI)
* Modular architecture

### Project Structure

```
task-manager-cli/
│
├── main.py          # CLI interface
├── task_service.py  # Task logic
├── storage.py       # JSON read/write operations
├── data.json        # Task storage file
├── .gitignore
└── README.md
```

### How to run the project

1. Clone the repository

```
git clone https://github.com/adriana762/task-manager-cli.git
```

2. Enter the project folder

```
cd task-manager-cli
```

3. Run the program

```
python main.py
```

### Example Usage

```
1- Create task
2- Complete task
3- Delete task
4- Show tasks
5- Exit

Choose an option: 1
Task title: Study Python
```

---

## About this project

This project was developed as part of my learning process in Python, focusing on:

* Writing clean and modular code
* Working with file persistence
* Using Git and GitHub for version control
