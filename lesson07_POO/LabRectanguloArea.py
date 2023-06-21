class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return self.altura*self.base
    
    
base=float(input('Ingrese base del rectangulo: '))
altura=float(input('Ingrese altura del rectangulo: '))
rectangulo=Rectangulo(base,altura)
print (f'El area del rectangulo es {rectangulo.calcular_area():.2f}')