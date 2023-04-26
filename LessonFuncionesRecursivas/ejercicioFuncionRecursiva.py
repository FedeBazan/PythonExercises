'''
Imprimir numeros de 5 a 1 de manera descendente usando funciones
recursivas. Puede ser cualquier valor positivo, ejemplo, si pasamos
el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir;
3
2
1

Si pasan valores negativos no imprime nada
'''

def imprimirNumeros(num):
    if num>=1:
        print (num)
        imprimirNumeros(num-1)
    elif num==0:
        return
    else:
        print ('Valor incorrecto')

numero=int(input('Ingrese numero positivo: '))
imprimirNumeros(numero)