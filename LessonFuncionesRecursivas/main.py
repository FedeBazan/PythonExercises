'''
Funcion que se llama asi misma para completar una accion
ejemplo clásico es el FACCTORIAL DE UN NUMERO
'''

def factorial(numero):
    if numero==1:
        return numero
    else:
        return numero * factorial(numero-1)

num=int(input('Ingrsa un numero: '))
print (f'El factorial de {num} es {factorial(num)}')