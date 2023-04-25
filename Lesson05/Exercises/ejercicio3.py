asignature=['Matemáticas', 'Física', 'Química','Historia','Lengua']
notas=[]
for materia in asignature:
    nota=int(input(f'Que nota te sacaste en {materia} : '))
    notas.append(nota)
for i in range(len(asignature)):
    print(f'En la materia {asignature[i]} te sacaste un {notas[i]}')