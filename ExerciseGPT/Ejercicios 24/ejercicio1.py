def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplicacion(x,y):
    return x*y
def division(x,y):
    return x/y

number1=int(input('Ingrese primer numero: '))
number2=int(input('Ingrese segundo numero: '))

print(f'''
Calculadora básica entre {number1} y {number2}:
1. Suma: {suma(number1,number2)}
2. Resta: {resta(number1,number2)}
3. Multiplicación: {multiplicacion(number1,number2)}
4. Division {division(number1,number2)}
''')