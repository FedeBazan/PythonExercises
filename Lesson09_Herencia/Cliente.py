from Persona import *

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad,id_cliente):
        super().__init__(nombre, apellido, edad)
        self.id_cliente=id_cliente

    def __str__(self):
        return print

cliente = Cliente('Fede','Apellido',31,'AJ08L')
print (cliente)