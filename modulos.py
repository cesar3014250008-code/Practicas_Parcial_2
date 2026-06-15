# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1 ():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("Apellido: ").strip().upper()
    print(f"El nombre del alumno es: {nombre} {apellidos}")

def borrarPantalla():
    print("\033c")

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f"El nombre del alumno es: {nombre} {apellidos}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe los apellidos: ").strip().upper()
    return nombre,apellidos
nom,ape=funcion2()
 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nombre,apellidos):
    nombre=nom
    apellidos=ape
    return nombre,apellidos

#Invocar las funciones
funcion1()

nombre=input("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
funcion3(nom,ape)

nombre,apellidos=funcion2()
print(f"El nombre del alumno es: {nombre} {apellidos}")

nombre=input("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
nom,ape=funcion4(nombre,apellidos)
print(f"El nombre del alumno es: {nom} {ape}")