import os
import modules.menu as m
from tabulate import tabulate
def GestionTr(trainers:dict,salones:dict,rutas:dict):
    n = m.MenuTrainers()
    if (n == 1):
        AddTrainer(trainers)
    elif (n == 2):
        AsignRoute(trainers,salones,rutas)
    elif (n == 3):
        pass

def AddTrainer(trainers:dict):
    isEmpty = True
    while isEmpty:
        os.system('cls')
        name = input('Ingrese el nombre del trainer nuevo: ')
        if bool(name)==True:
            isEmpty = False
    id = str(len(trainers)+1).zfill(3)
    trainer = {
        'nombre':name,
        'rutas':{}
    }
    trainers.update({id:trainer})
    print(f'el trainer {name} fue agregado con el id {id}')
    os.system('pause')

def AsignRoute(trainers:dict,salones:dict,rutas:dict):
    id = ValidateId(trainers)
    if bool(id) == True:
        print('seleccione el salon donde se encuentra la ruta')
        os.system('pause')
        n = m.MenuSalones()
        if (n == 1):
            sln = salones.get('apolo')
            salon = 'apolo'
        elif (n == 2):
            sln = salones.get('sputnik')
            salon = 'sputnik'
        elif (n == 3):
            sln = salones.get('artemis')
            salon = 'artemis'
        dcTrainer = trainers.get(id)
        
        lsOp = list(sln.values())
        isExist = True
        if (len(sln) != 0):
            while isExist: 
                os.system('cls')
                print(f'ingrese el (id salon) de la ruta del salón {salon} que quiere agregar')
                print(tabulate(lsOp,headers="keys",tablefmt="grid"))
                nr = input(')..')
                if (nr in sln):
                    add = sln.get(id)
                    na = add.get('nombre')
                    route = add.get('id ruta')
                    rt = rutas.get(na)[route]
                    add['trainer'] = dcTrainer['nombre']
                    rt['trainer'] = dcTrainer['nombre']
                    isExist = False
                    dcTrainer['rutas'].update({str(len(dcTrainer['rutas'])+1):add})
                else:
                    print('id inválido')
                    os.system('pause')
        else:
            os.system('cls')
            print('Este salón no tiene rutas agregadas, intente con otro')
            os.system('pause')
    else:
        pass
        

def ValidateId(trainers:dict):
    os.system('cls')
    id = input('Ingrese el id del trainer al que le desea agregar rutas: ')
    if (len(trainers) == 0):
        return
    elif (id not in trainers):
        print('ID de trainer no fue encontrado')
        os.system('pause')
    else:
        return id