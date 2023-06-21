class Persona:
    def __init__(self,nombre,apellido,edad):
        self.__nombre=nombre #el encapsulamiento de una variable se marca con __
        self.__apellido=apellido
        self.__edad=edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido (self,apellido):
        self.__apellido=apellido

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    def __del__(self):
        print (f'Se elimina {self.__apellido} {self.__nombre} {self.edad}')

    def saludar(self):
        print (f'Hola {self.apellido} {self.__nombre}, tienes {self.edad} años')

if __name__ == '__main__':

    persona1=Persona('Fede', 'Bazan' ,31)
    persona1.saludar()

    print(f'__ESTE ES EL SEGUNDO SALUDO__ : Hola {persona1.apellido} {persona1.nombre}, tienes {persona1.edad} años')

    persona1.apellido = 'Schokorztka'
    persona1.nombre = 'Anatoly'
    persona1.edad = 50

    print(f'__ESTE ES EL SEGUNDO SALUDO__ : Hola {persona1.apellido} {persona1.nombre}, tienes {persona1.edad} años')

    #hacer el metodo GET y SET para la clase persona
    #una variable que no tiene el metodo SET es considerada solo un atributo de LECURA