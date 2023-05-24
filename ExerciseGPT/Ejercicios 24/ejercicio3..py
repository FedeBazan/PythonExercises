def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def confirmacion(num):
    while num <= 0:
        num = int(input('Ingrese un número mayor que 0: '))
    return num

numero=int(input('Numero para obtener el factorial: '))
numero=confirmacion(numero)
print (f'El factorial de {numero} es {factorial(numero)}')