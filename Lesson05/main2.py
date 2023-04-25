'''
-no mantiene un orden
-no permite almacenar elemnto duplicados
-no se puede alterar los elementos adentro
-se pueden agregar o eliminar elementos
-no tienen un indice
'''

planetas = {'Marte','Jupiter','Venus'}
print(planetas)

#largo
print(len(planetas))
#revisar si un elemento esta presente
print('Marte' in planetas)
#agregar elementos
planetas.add('Tierra')
print(planetas)
# no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elemento
planetas.remove('Tierra')
#planetas.discard() elimiinar elementonos pero no arroja error
print(planetas)

#limpiar el set
planetas.clear()
print(planetas)

#eliminar el set
del planetas
print(planetas)