'''

class Persona:
    def __init__(self):
        self.nombre='Juan'
        self.apellido='Përez'
        self.edad=28


persona1=Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

'''
class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def mostrarInformacion(self):
        print(f'Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad:{self.edad}')

persona1=Persona('Fede','Bazan',31)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad) 

persona2=Persona('Karla','Gomez',30)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona1.nombre='Julio Pablo Federico'
print (f'Nombre: {persona1.nombre}\nApellido: {persona1.apellido}\nEdad:{persona1.edad}')

'''
se definio un metodo que muestra los datos que se otorgo al objeto previamente
'''
print('------')
persona1.mostrarInformacion()