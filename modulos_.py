# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")

def solicitar_nombre():
    name=input("Ingrese el nombre por favor: ")
    apellido=input("Ingrese el apellido por favor: ")

    return name,apellido