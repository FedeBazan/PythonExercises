'''
Ejercicio de calculadora de impuestos
Crear una función para calcular el total de un pago incluyendo
un impuesto aplicado.
Formula: pago_total=pago_sin_impuesto+pago_sin_impuesto*(impuesto/100)
'''
def totalAPagar (pago,impuesto):
    return round(pago+pago*(impuesto/100),2)

pago=float(input('Ingrese el pago sin impuesto aplicado: '))
impuesto=int(input('Ingrese el % de impuesto a aplicar: '))
print(f'Total a pagar es de {totalAPagar(pago,impuesto)}')
