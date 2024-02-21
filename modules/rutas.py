import os
import modules.menu as m
import random
def nwRoute(rutas:dict,salones:dict):
    fundamentos=[]
    web=[]
    formal=[]
    bd=[]
    backend=[]
    os.system('cls')
    print('Seleccione el tipo de ruta que va a crear')
    os.system('pause')
    x = m.MenuRutas()
    if (x == 1):
        rt = rutas.get('Java')
        tipo = 'Java'
    elif (x == 2):
        rt = rutas.get('NodeJs')
        tipo = 'NodeJs'
    elif (x == 3):
        rt = rutas.get('NetCore')
        tipo = 'NetCore'
    print('Seleccione el salon donde se va a enseñar la nueva ruta')
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
    inicio = input('ingrese la fecha de inicio de la ruta: ')
    fin = input('ingrese la fecha de finalización de la ruta: ')
    addFundamentos(fundamentos)
    addWeb(web)
    addFormal(formal)
    addBd(bd)
    addBackend(backend)
    id = random.randint(1,100)
    idSln = str(len(sln)+1).zfill(3)
    nwRt={
        'id ruta':id,
        'nombre':tipo,
        'fundamentos':{
            'lenguajes':fundamentos,
            'notas':{}     
        },
        'web':{
            'lenguajes':web,
            'notas':{}
        },
        'formal':{
            'lenguajes':formal,
            'notas':{}
        },
        'bd':{
            'lenguajes':bd,
            'notas':{}
        },
        'backend':{
            'lenguajes':backend,
            'notas':{}  
        },
        'trainer':'',
        'salon':salon,
        'inicio ruta':inicio,
        'fin ruta':fin
    }
    nwSln={
        'id salon':idSln,
        'id ruta':id,
        'nombre':tipo,
        'fundamentos':fundamentos,
        'web':web,
        'formal':formal,
        'bd':bd,
        'backend':backend,
        'trainer':'',
        'salon':salon,
        'cupo':33,
        'inicio ruta':inicio,
        'fin ruta':fin
    }
    rt.update({id:nwRt})
    sln.update({idSln:nwSln})

def addFundamentos(fundamentos:list):
    isEmpty=True 
    while isEmpty:
        os.system('cls')
        name = input('Ingrese temática de fundamentos: ')
        if bool(name) == True:
            isEmpty = False
    fundamentos.append(name)
    rp = bool(input('Desea agregar otra temática? S(si) o Enter(no)'))
    if (rp ==True):
        addFundamentos(fundamentos)
    else:
        pass
    
def addWeb(web:list):
    isEmpty=True
    while isEmpty:
        os.system('cls')
        name = input('Ingrese temática de Progrmación web: ')
        if bool(name) == True:
            isEmpty = False
    web.append(name)
    rp = bool(input('Desea agregar otra temática? S(si) o Enter(no)'))
    if (rp ==True):
        addWeb(web)
    else:
        pass

def addFormal(formal:list):
    isEmpty=True
    while isEmpty:
        os.system('cls')
        name = input('Ingrese temática de Progrmación formal: ')
        if bool(name) == True:
            isEmpty = False
    formal.append(name)
    rp = bool(input('Desea agregar otra temática? S(si) o Enter(no)'))
    if (rp ==True):
        addFormal(formal)
    else:
        pass

def addBd(bd:list):
    isEmpty=True
    while isEmpty:
        os.system('cls')
        name = input('Ingrese temática de bases de datos: ')
        if bool(name) == True:
            isEmpty = False
    bd.append(name)
    rp = bool(input('Desea agregar otra temática? S(si) o Enter(no)'))
    if (rp ==True):
        addBd(bd)
    else:
        pass

def addBackend(backend):
    isEmpty=True
    while isEmpty:
        os.system('cls')
        name = input('Ingrese temática de Backend: ')
        if bool(name) == True:
            isEmpty = False  
    backend.append(name)
    rp = bool(input('Desea agregar otra temática? S(si) o Enter(no)'))
    if (rp ==True):
        addBackend(backend)
    else:
        pass