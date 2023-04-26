def suma(x,y):
    return x+y
print('Suma entre 2 numeros')
a=int(input('Ingresa un número: '))
b=int(input('Ingresa otro número: '))
print(f'La suma entre {a} y {b} es: {suma(a,b)}')
print('---------------')


def sumarValores (*x):
    sum=0
    for numeros in x:
        sum += numeros
    else:
        return sum


c=int(input('Ingresa otro numero mas: '))
print(f'La suma entre los numeros {a}, {b} y {c} es : {sumarValores(a,b,c)}')