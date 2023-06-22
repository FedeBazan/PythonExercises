class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    

class Empleado(Persona):
    def __init__(self, nombre, apellido, edad,sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo=sueldo

    def mostrar_datos_empleado(self):
        print (f'DATOS EMPLEADO \n APELLIDO y NOMBRE: {self.apellido}, {self.nombre}\n EDAD: {self.edad}\n SUELDO: {self.sueldo:.2f} ')

if __name__=='__main__':

    print('Registro de empleado')
    nombre=input ('Coloque su nombre: ')
    apellido= input ('Coloque su apellido: ')
    edad=int(input('Edad: '))
    sueldo=float(input('Ingrese sueldo: '))

    empleado1=Empleado(nombre,apellido,edad,sueldo)
    empleado1.mostrar_datos_empleado()