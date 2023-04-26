'''
Ejercicio: convertidor de Temperatura
Realizar dos funciones para convertir de grados Celicius a Fanhrenheit y viceversa.
'''

def celciusAFahrenheit(temp):
    print(f'La temperatura {temp}°C es {temp*1.8+32}°F')

def fahrenheitACelcius(temp):
    print(f'La temperatura {temp}°F es {(temp-32)*(5/9)}')


opc=int(input('''---Elija la opcion---
1-Convertir de Grado Celcius a Fahrenheit
2-Convertir de Grado Fahrenheit a Celcius
'''))
if opc==1:
    temp=float(input('Temperatura en Celcius: '))
    celciusAFahrenheit(temp)
elif opc==2:
    temp=float(input('Temperatura en Fahrenheit: '))
    fahrenheitACelcius(temp)
else:
    print('Opcion ERRONEA')
