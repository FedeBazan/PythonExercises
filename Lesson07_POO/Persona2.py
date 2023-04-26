class Persona:
    def __init__(self,nombre,apellido,edad,*valores,**masdatos):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.valores=valores
        self.masdatos=masdatos

    def mostrarInformacion(self):
        print(f'Nombre completo: {self.apellido}, {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Muestra tupla: {self.valores}')
        print(f'Muestra diccionario: {self.masdatos}')

persona=Persona('Julio Pablo Federico','Bazan',31,'valor 1 de tupla','valor 2 de tupla',m='manzana',n='naranja')
persona.mostrarInformacion()