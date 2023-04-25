#pasar un diccionario a la funcion y escribir los valores

def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos(IDE='Integrated Develompent Enviroment',PK='Primary Key')
listarTerminos(DBMS = 'Database Management System')

