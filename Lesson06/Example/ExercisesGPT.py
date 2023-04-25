#1 Crear un diccionario vacio y agregar un par clave-valor
print('Ejercicio 1')
my_dict = {}
my_dict['key1'] = 'llave 1'
print (my_dict)
my_dict.clear()

#2 Crear un diccionario con varias Key-Values
print ('Ejercicio 2')
my_dict = {'key1':'value1','key2':'value2','key3':'value3'}
print(my_dict)
my_dict.clear()

#3 Acceder a un valor en un diccionario mediante su clave
print('Ejercicio 3')
my_dict={'key1':'value1','key2':'value2','key3':'value3'}
print(my_dict['key1'])
my_dict.clear()

#4 Eliminar un par clave-valor
print('Ejercicio4')
my_dict={'key1':'value1','key2':'value2','key3':'value3'}
del my_dict['key2']
print (my_dict)
my_dict.clear()

#5 Recorrer un diccionario e imprimir todas sus claves
print('Ejercicio 5')
my_dict={'key1':'value1','key2':'value2','key3':'value3'}
for keys in my_dict:
    print (keys)
my_dict.clear

#6 Recorrer un diccionario e imprimir todas sus claves
print('Ejercicio 6')
my_dict={'key1':'value1','key2':'value2','key3':'value3'}
