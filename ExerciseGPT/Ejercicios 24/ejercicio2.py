def centimetros(metros):
    return metros*100
def pulgadas(metros):
    return metros*39.37
def pies(metros):
    return metros*3.28084

metros=float(input('Ingresa la cantidad de metros para convertir: '))
print(f'''
---Conversor de Unudades---
Metros: {round(metros,2)} m.
Centimetros: {round(centimetros(metros),2)} cm.
Pulgadas: {round(pulgadas(metros),2)} pulgadas
Pies: {round(pies(metros),2)} pies
''')
