class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        print(f'El area del rectangulo: {round(self.base*self.altura,2)}cm.**2')

base=float(input('Ingresa la medida de la base(cm): '))
altura=float(input('Ingresa la medida de la altura(cm): '))
rectangulo=Rectangulo(base,altura)
rectangulo.area()