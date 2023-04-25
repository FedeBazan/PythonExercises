materias=[]
respuesta=input('¿Desea agregar una materia?(SI/NO): ')
respuesta2='si'

if respuesta.lower()=='si':
    while respuesta2.lower()=='si':
        materia=input('Escriba la materia a agregar: ')
        materias.append(materia)
        respuesta2=input('¿Desea agregar otra materia?(SI/NO): ')
        while respuesta2.lower() != 'si' and respuesta2.lower() != 'no':
            respuesta2 = input('De una respuesta valida (SI/NO): ')
    else:
        if respuesta2.lower()=='no':
            print('Se terminaron de agregar materias')
            for mate in materias:
                print(mate)
            print('Fin del Programa')
elif respuesta.lower()=='no':
    print('No se agregaron materias')
    print('Fin del Programa')
else:
    print('No se reconoce respuesta')
    print('Fin del Programa')