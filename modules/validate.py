import os
def ValidateInt()->int:
    try:
        x = int(input(')..'))
    except ValueError:
        print('El valor ingresado no es válido')
        os.system('pause')
        return ValidateInt()
    else:
        return x
    
def ValidateFloat()->float:
    try:
        x = float(input(')..'))
    except ValueError:
        print('El valor ingresado no es válido')
        os.system('pause')
        return ValidateFloat()
    else:
        return x
    
def ValidateId(campers:dict):
    os.system('cls')
    id = input('Ingrese el id del camper: ')
    if (len(campers) == 0):
        print('Aún no ha agregado campers')
        return
    elif (id not in campers):
        print('ID de camper no fue encontrado')
        os.system('pause')
        ValidateId(campers)
    else:
        return id