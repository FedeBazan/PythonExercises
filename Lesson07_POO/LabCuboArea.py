class Cubo:
    def __init__(self,lado):
        self.lado=lado

    def calcular_area_cubo(self):
        return (self.lado**3)
    
lado=float(input('Ingrese el valor de la arista: '))
cubo=Cubo(lado)
print (f'El area del Cubo es de {cubo.calcular_area_cubo():.2f}')