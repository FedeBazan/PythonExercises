'''
def miFuncionEnPython(nombre,apellido):
    print(f'Saludos {nombre} {apellido} desde mi funcion')
miFuncionEnPython('Fede','Bazan')

def suma (x,y):
    return  x+y
print(f'La suma de 2 y 3 es: {suma(2,3)}')

def sumar (a=0,b=0) -> int:
    return a+b
print(f'la suma de 2 y 8 es: {sumar(2,8)}')
print(f'la suma de los parametros default: {sumar()}')
'''
def listaDeNombres (*nombres):
    for nombre in nombres:
        print(nombre)

listaDeNombres('Mario','Karla','Satto','Vicky')
listaDeNombres('Jorge','Cintia','Andrea')
print('codecaps')