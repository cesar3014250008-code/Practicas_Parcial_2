"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

set1={"Python", "SOL", "Estructurado", "SQL"}
print(set1)

for i in set1:
    print(i)
  
set2={"Hola",True,33,3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={""}
print(set3)

set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)

lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=list(conjunto)
print(lista)


#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados
resp="S"

while resp=="S":
    emails=[]
    resp2="Si"
    while resp2=="Si":
        emails.append(input("Email: "))
        resp2=input("Otra email? ").capitalize().strip()
    emails_2=set(emails)
    print(emails_2)
    resp=(input("Otra captura (S/N)? ")).upper().strip()
#Solucion 1
list_email=[]

opc="S"

while opc=="S":
    list_email.append(input("Ingresa un email: ").lower().strip())
    opc=input("Deseas ingresar otro email (S/N)? ").upper().strip()
print(list_email)

set_emails=set(list_email)
list_emails=list(set_emails)
print(list_emails)
#Solucion 2

list_email=[]

opc=True

while opc:
    list_email.insert(0,input("Ingrese un email: ").lower().strip())
    opc=input("Deseas ingresar otro email (S/N)? ").upper().strip()
    if opc=="N":
        opc=False

print(list_email)

list_email=[]

opc="S"

while opc=="S":
    list_email.append(input("Ingresa un email: ").lower().strip())
    opc=input("Deseas ingresar otro email (S/N)? ").upper().strip()
print(list_email)
set_emails=set(list_email)
list_emails=list(set_emails)
print(list_emails)





