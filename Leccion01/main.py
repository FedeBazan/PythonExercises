import self as self
import values as values

print("Este es mi saludo desde python")
#delaracion de variable

miVariable = 3
print(miVariable)

miVariable = 2
print(miVariable)

x=10
y=2
z=x+y

print(x)
print(y)
print(z)
print(x+y)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print("Hola victoria")



def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
for i in range(10):
    pairs.sort(key = lambda pair:pair[1])
    print(pairs)

class Mapping:
    def __int__(self,iterable):
        self.items_list=[]
        self.__update(iterable)

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update()

class MappingSubclass(Mapping):
    for item in zip (keys,values):
        self.item_list.append(item)

print('finished')