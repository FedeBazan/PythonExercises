# Diccionarios
print('hola mundo')
diccionario={
    'Azul':'Blue',
    'Rojo':'Red',
    'Verde':'Green'
}

#Se agrega un elemento en un diccionario
diccionario['Amarillo']='Yellow'
print(diccionario)

#Eliminar un elemento del diccionario
del(diccionario['Amarillo'])

print(diccionario)

#diccionario guardando lista

diccionario={
    'Alejandro':[21,1.73],
    'Jose':[21,1.75],
    'Maria':[22,1.67]
}
print(diccionario)

#diccionario guardando otro diccionario

diccionario={
    'Alejandro':{'Edad':21,'Estatura':1.73},
    'Jose':{'Edad':21,'Estatura':1.75},
    'Maria':{'Edad':22,'Estatura':1.67}
}

print(diccionario)

#diccionario con key int

equipo  = {
    10:'Dybala',
    11:'Douglas',
    7:'Rumaldo'
}

print(equipo[10])