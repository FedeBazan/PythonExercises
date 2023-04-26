class Cubo:
    def __init__(self,ancho,alto,profundo):
        self.ancho=ancho
        self.alto=alto
        self.profundo=profundo

    def area(self):
        print(f'El area del cubo es de: {round(self.alto*self.ancho*self.profundo,2)} cm**3 (Aprox.)')

ancho=float(input('Ingrese la medida del ancho(en cm.): '))
alto=float(input('Ingrese la medida del alto(en cm.): '))
profundo=float(input('Ingrese la medida de lo profundo(en cm.): '))

cubo=Cubo(ancho,alto,profundo)
cubo.area()