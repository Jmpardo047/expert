import os
import modules.menu as m
from tabulate import tabulate
def Reps(campers:dict,salones:dict,rutas:dict,trainers:dict):
    x = m.MenuReps()
    if (x == 1):
        Inscritos(campers)
    elif (x == 2):
        Aprobados(campers)
    elif (x == 3):
        TrainersLst(trainers)
    elif (x == 4):
        Riesgo(campers)
    elif (x == 5):
        RouteLst(campers,trainers,salones)
    elif (x == 6):
        LstModule(salones,rutas)
    elif (x == 7):
        pass
def Inscritos(campers:dict):
    os.system('cls')
    inscrito =[]
    for keys,values in campers.items():
        if ('inscrito' in values['estado']):
            inscrito.append(campers[keys]['nombre'])
    print('Campers que se encuentan inscritos:')
    for items in inscrito:
        print(items)
    os.system('pause')

def Aprobados(campers:dict):
    os.system('cls')
    aprobado =[]
    for keys,values in campers.items():
        if ('aprobado' in values['estado']):
            aprobado.append(campers[keys]['nombre'])
    print('Campers que fueron aprobados:')
    for items in aprobado:
        print(items)
    os.system('pause')

def TrainersLst(trainers:dict):
    os.system('cls')
    lst = list(trainers.values())
    print('trainers que se encuentran registrados:')
    print(tabulate(lst,headers="keys",tablefmt="grid"))
    os.system('pause')

def Riesgo(campers:dict):
    os.system('cls')
    riesgo =[]
    for keys,values in campers.items():
        if ('riesgo' in values['estado']):
            riesgo.append(campers[keys]['nombre'])
    print('Campers que se encuentan en riego:')
    for items in riesgo:
        print(items)
    os.system('pause')

def LstModule(salones:dict,rutas:dict):
    os.system('cls')
    print('seleccione el salón donde se encuentra la ruta')
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
    lsOp = list(sln.values())
    os.system('cls')
    print(f'ingrese el (id ruta) de la ruta que quiere buscar')
    print(tabulate(lsOp,headers="keys",tablefmt="grid"))
    nr = int(input(')..'))
    for key,value in rutas.items():
        for v1,v2 in value.items():
            if (nr == v1):
                rt = rutas.get(key)[nr]
    modulo = m.MenuModulos()
    if (modulo == 1):
        mod = rt.get('fundamentos')['notas']
    elif (modulo == 2):
        mod = rt.get('web')['notas']
    elif (modulo == 3):
        mod = rt.get('formal')['notas']
    elif (modulo == 4):
        mod = rt.get('bd')['notas']
    elif (modulo == 5):
        mod = rt.get('backend')['notas']
    lt = list(mod.values())
    print(tabulate(lt,headers="keys",tablefmt="grid"))
    os.system('pause')
    

def RouteLst(campers:dict,trainers:dict,salones:dict):
    os.system('cls')
    print('seleccione el salón donde se encuentra la ruta')
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
    lsOp = list(sln.values())
    os.system('cls')
    print(f'ingrese el (id ruta) de la ruta que quiere buscar')
    print(tabulate(lsOp,headers="keys",tablefmt="grid"))
    nr = int(input(')..'))
    lst={
    'id ruta':nr,
    'trainer':'',
    'campers':[]
    }
    for keys,values in campers.items():
        routeCamper = campers.get(keys)
        verR = routeCamper['ruta'].values()
        if (nr in verR):
            lst['campers'].append(routeCamper['nombre'])
    for keys,values in trainers.items():
        routeTrainer = trainers.get(keys)['rutas']
        for key,value in routeTrainer.items():
            ps = routeTrainer.get(key)
            if (nr in ps.values()):
                lst['trainer'] = values['nombre']
    camps = lst.get('campers')
    os.system('cls')
    print('estos son los campers y trainer asociados con la ruta {nr}')
    print(f'trainer : {lst["trainer"]}')
    print('---Campers---')
    for items in camps:
        print(items)
    os.system('pause')
    

