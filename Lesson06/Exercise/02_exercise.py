def multiplicar(x,y):
    return x*y
print('Multiplicacion entre 2 numeros')
a=int(input('Ingresa un número: '))
b=int(input('Ingresa otro número: '))
print(f'La multiplicacion entre {a} y {b} es: {multiplicar(a,b)}')
print('---------------')


def multiplicarValores (*x):
    mul=1
    for numeros in x:
        mul *= numeros
    else:
        return mul


c=int(input('Ingresa otro numero mas: '))
print(f'La multiplicacon entre los numeros {a}, {b} es {multiplicar(a,b)} y si lo multiplicamos por {c} es : {multiplicarValores(a,b,c)}')