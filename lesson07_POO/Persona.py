class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def saludar(self):
        print (f'Hola {self.apellido} {self.nombre}, tienes {self.edad} años')

persona1=Persona('Fede', 'Bazan' ,31)
persona1.saludar()

persona1.nombre='Mojo'
persona1.apellido='Jojo'
persona1.edad=50
persona1.saludar()

persona1.nombre=input('Give me ur name: ')
persona1.apellido=input('Chop chop moron, surname: ')
persona1.edad = input('Age of empire: ')
persona1.saludar()