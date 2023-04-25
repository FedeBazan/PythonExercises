#Definir lista
nombres= ['juan','carla','Ricardo','Maria']
#Imprimir la lista de nombres
print(nombres)
#Acceder a los elementos  de una lista
print(nombres[0])
print(nombres[2])
#Acceder a los elementos de manera inversa
print(nombres[-1]) #Acceder al ULTIMO ELEMENTO DE LA LISTA
#imprimir un rango
print(nombres[0:2]) #sin incluir el indice 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
#Desde el indice indicado hasta el final
print(nombres[1:])
#cambiar el valor
nombres[3]='Ivone'
print(nombres)
#iteracion de lista
for nombre in nombres: #nombre es una variable de iteracion
    print(nombre)
else:
    print('No existen mas nombres en la lista')
#preguntar el LARGO de una lista
print(len(nombres))
#agregar un elemento en una lista
nombres.append('Lorenzo')
print(nombres)
#insertar un elemento en un indice en especifico
nombres.insert(1,'Octavio')
print(nombres)
#remover un elemeneto
nombres.remove('Octavio')
print(nombres)
#remover el ULTIMO valor agregado
nombres.pop()
print(nombres)
#eliminar un indice indicado
del nombres[0]
print(nombres)
#LIMPIAR ELEMENTOS DE LA LISTA
nombres.clear()
print(nombres)
#borrar la lista por completo
del nombres
print(nombres)
