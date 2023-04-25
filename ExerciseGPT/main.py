#---exercise 1--- Crea una lista vacía y añade 5 elementos de cualquier tipo.
import random

lista=[]
for i in range(10):
    numero=random.randint(1,100)
    lista.append(numero)
else:
    print(lista)

#---exercise 2--- Crea una tupla de números y ordénalos de mayor a menor.
lista.clear()
tuplaDeNumero=(10,39,49,62,24,2,50,100)
lista=list(tuplaDeNumero)
print(lista)
print(sorted(lista, reverse=True))

#---exercise 3--- Crea un diccionario con 5 elementos, donde las llaves sean nombres y los valores sean edades.

registro={
    'Nombre1':10,
    'Nombre2':2,
    'Nombre3':40,
    'Nombre4':35,
    'Nombre5':14
}
print(registro)

#---exercise 4--- Crea una función que reciba una lista y devuelva la suma de todos sus elementos.

def sumar(X):
    laSuma=0
    for i in range(len(X)):
        laSuma+=X[i]
    else:
        return laSuma

print(f'La suma de todos los elementos de la lista es {sumar(lista)}')

#---exercise 5---

def mayor(X):
    maximo=0
    for i in range(len(X)):
        if X[i]>maximo:
            maximo=X[i]
    else:
        return maximo
print(f'El mayor de los numeros de una tupla {mayor(tuplaDeNumero)}')

#---exercise 6---