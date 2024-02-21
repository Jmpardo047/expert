import os 
import modules.menu as m
import modules.validate as v
from tabulate import tabulate
def GestCampers(campers:dict,salones:dict):
    n = m.MenuCampers()
    if (n == 1):
        addCamper(campers)
    elif (n == 2):
        AsignCamper(campers,salones)
    elif (n == 3):
        pass
def addCamper(campers:dict):
    isExist = True
    os.system('cls')
    nombre = input('Ingrese el nombre del camper: ').upper()
    apellido = input('Ingrese los apellidos del camper: ').upper()
    while isExist:
        doc = input('Ingrese el número de documento de identidad del camper: ')
        if (doc not in campers):
            isExist = False
        else:
            print('este documento ya fue ingresado')
    direccion = input('Ingrese la dirección del camper: ')
    acudiente = AcudientInfo()
    telefono =input('Ingrese el número de teléfono del camper: ')
    celular = input('Ingrese el número de teléfono celular del camper: ')
    nwCamper = {
        'id':doc,
        'nombre':nombre,
        'apellidos':apellido,
        'direccion':direccion,
        'acudiente':acudiente,
        'teléfono':telefono,
        'celular':celular,
        'estado':'inscrito'
    }
    campers.update({doc:nwCamper})

def AcudientInfo()->dict:
    nombre = input('Ingrese el nombre completo del acudiente: ').upper()
    cc = input('Ingrese el número de documento del acudiente: ')
    print('Ingrese el número de contacto sin espacios del acudiente: ')
    tel = v.ValidateInt()
    ac = {
        'nombre':nombre,
        'documento': cc,
        'teléfono' : tel
    }
    return ac

def AsignCamper(campers:dict,salones:dict):
    os.system('cls')
    print('Ingrese el id del camper:')
    id = v.ValidateId(campers)
    if bool(id) == True:
        if(campers[id]['estado'] == 'aprobado'):
            print('Seleccione el salón donde se va a inscribir al camper:')
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
            dcCamper = campers.get(id)
            lsOp = list(sln.values())
            isExist = True
            if (len(sln) != 0):
                while isExist:
                    os.system('cls')
                    print(f'ingrese el (id salon) de la ruta del salón {salon} donde quiere inscribir al camper:')
                    print(tabulate(lsOp,headers="keys",tablefmt="grid"))
                    nr = input(')..')
                    rt = sln.get(nr)
                    if (nr in sln):
                        if(sln[nr]['cupo'] != 0):
                            campers[id].update({'ruta':rt})
                            sln[nr]['cupo'] -= 1
                            isExist = False
                        else:
                            print('el cupo para este curso ya se ha agotado')
                            os.system('pause')
                    else:
                        print('id inválido')
                        os.system('pause')
            else:
                os.system('cls')
                print('Este salón no tiene rutas agregadas, intente con otro')
                os.system('pause')
        else:
            os.system('cls')
            print('Este camper aun no ha sido aprobado')
            os.system('pause')
    else:
        pass