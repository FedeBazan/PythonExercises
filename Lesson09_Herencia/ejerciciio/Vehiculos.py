class Vehiculo:
    def __init__(self,color,ruedas,rodado):
        self.rodado=rodado
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return f'Tipo de Rodado: {self.rodado}\n Color: {self.color}\n Cantidad de ruedas: {self.ruedas} '
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, rodado,velocidad):
        super().__init__(color, ruedas, rodado)
        self.velocidad=velocidad

    def __str__(self):
        return f'{super().__str__()}\n Velocidad: {self.velocidad} km/h'
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, rodado,tipo_bici):
        super().__init__(color, ruedas, rodado)
        self.tipo_bici=tipo_bici

    def __str__(self):
        return f'{super().__str__()}\n Tipo de Bicicleta: {self.tipo_bici}'
    
volkswagen=Coche('Negro',4,'Auto',190)
print ('VEHICULO'.center(50,'*'))
print(volkswagen)

bmx=Bicicleta('Rojo',2,'Bicicleta','Montaña')
print ('BICICLETA'.center(50,'*'))
print(bmx)