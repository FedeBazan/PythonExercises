numerosGanadores=[]
bandera='si'

while bandera.lower()=='si':
    numero=int(input('Agregue numero ganador: '))
    numerosGanadores.append(numero)
    bandera=input('Hay otro numero ganador?(SI/NO): ')
    while bandera.lower() != 'si' and bandera.lower() != 'no':
        bandera = input('De una respuesta valida (SI/NO): ')
else:
    numerosGanadores.sort()
    print(f'Lista Ordenada de numeros ganadores: {numerosGanadores}')