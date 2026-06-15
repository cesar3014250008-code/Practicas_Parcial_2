"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
print("\033c")

#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]


#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[0]+" "+paises[3])

#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)

# #2do forma 
for i in range(0,5):
    print(paises[i])


paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
#ordenar elementos de una lista
paises.sort() #ordena de manera acendente
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)


paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Argentina")
print(paises)
paises.insert(100,"Panama")
print(paises)
paises.append(23)
paises.append(3)
print(paises)
paises.sort() #no se puede aplicar cuando los datos son diferenter
print(paises)


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma 
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
buscar="Brazil" in paises
if buscar==True:
    print("Soy True")
else:
    print("Soy False")


#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,24,8,23,50,23]
num=int(input("Dame un numero a contar: "))
cuantas=numeros.count(num)
print(f"El numero {num} aparece: {cuantas} veces")



#Conocer la posicion o indice en el que se encuentra un elemento de la lista
pocision=numeros.index(50)
print(f"Estoy en la pocision: {pocision}")



#Unir el contenido de una lista dentro de otra lista
numeros1=[23,45,24,8,23,50,23]
numeros2=[100,-100]
numeros1.extend(numeros2)
print(numeros1)


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros1.sort()
numeros.reverse()
print(numeros1)



