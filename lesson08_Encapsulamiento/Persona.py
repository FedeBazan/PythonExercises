class Persona:
    def __init__(self,nombre,apellido,edad):
        self.__nombre=nombre #el encapsulamiento de una variable se marca con __
        self.apellido=apellido
        self.edad=edad
    
    def saludar(self):
        print (f'Hola {self.apellido} {self.__nombre}, tienes {self.edad} años')

persona1=Persona('Fede', 'Bazan' ,31)
persona1.saludar()

persona2=Persona('Rocke','Anatoly',12)
persona2.saludar()

#hacer el metodo GET y SET para la clase persona