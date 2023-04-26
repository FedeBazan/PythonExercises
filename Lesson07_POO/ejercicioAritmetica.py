class Aritmetica:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sumar(self):
        print(f'la suma entre {self.num1} y {self.num2} es: {self.num1+self.num2}')
    
    def restar(self):
        print(f'La resta entre {self.num1} y {self.num2} es: {self.num1-self.num2}')
    
    def multiplicar(self):
        print(f'La multiplicacion entre {self.num1} y {self.num2} es: {self.num1*self.num2}')
    
    def dividir(self):
        print(f'La division entre {self.num1} y {self.num2} es: {round(self.num1/self.num2,2)}')
    
operadorA=int(input('Ingresa el primer operador: '))
operadorB=int(input('Ingresa el segundo operador: '))

operadores=Aritmetica(operadorA,operadorB)
operadores.sumar()
operadores.restar()
operadores.multiplicar()
operadores.dividir()