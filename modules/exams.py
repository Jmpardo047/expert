import os
import modules.menu as m
import modules.validate as v
def GestorEx(campers:dict,rutas:dict):
    n = m.MenuExams()
    if (n == 1):
        ExamenIngreso(campers)
    elif (n == 2):
       ExamenModulo(campers,rutas)
    elif (n == 3):
        pass
def ExamenIngreso(campers:dict):
    os.system('cls')
    id = v.ValidateId(campers)
    if bool(id) == True:
        if (campers[id]['estado'] == 'inscrito'):
            print('Ingrese la nota que obtuvo en el examen práctico')
            pr = v.ValidateFloat()
            print('Ingrese la nota que obtuvo en el examen teórico')
            te = v.ValidateFloat()
            nFinal = (pr+te)/2
            if (nFinal >= 60):
                campers[id]['estado'] = 'aprobado'
            else:
                campers[id]['estado'] = 'reprobado'
        else:
            os.system('cls')
            print('A este camper ya se le aplico la prueba de ingreso')
            os.system('pause')
    else:
        pass

def ExamenModulo(campers:dict,rutas:dict):
    os.system('cls')
    id = v.ValidateId(campers) 
    if bool(id) == True:
        isExist = True
        try:
            idRuta = campers.get(id)['ruta']['id ruta']
            nameRuta = campers.get(id)['ruta']['nombre']
            ruta = rutas.get(nameRuta)[idRuta]
        except KeyError:
            isExist = False
            return
        name = campers.get(id)['nombre']
        if(bool(ruta['trainer']) == True):
            if (isExist == True):
                x = m.MenuModulos()
                if (x == 1):
                    mod = ruta.get('fundamentos')['notas']
                elif (x == 2):
                    mod = ruta.get('web')['notas']
                elif (x == 3):
                    mod = ruta.get('formal')['notas']
                elif (x == 4):
                    mod = ruta.get('bd')['notas']
                elif (x == 5):
                    mod = ruta.get('backend')['notas']
                print('Ingrese la nota del exámen práctico')
                pr = v.ValidateFloat()
                print('Ingrese la nota del exámen teórico')
                te = v.ValidateFloat()
                print('Ingrese la nota del los trabajos')
                tb = v.ValidateFloat()
                total = (pr*0.6)+(te*0.3)+(tb*0.1)
                os.system('cls')
                print(f'la nota final de el estudiante fue {total}')
                os.system('pause')
                if(total>60):
                    campers[id]['estado'] = 'aprobado'
                    addNote = {
                    'nombre':name,
                    'nota':total,
                    'tipo':'aprobado'
                    }
                else:
                    campers[id]['estado'] = 'riesgo'
                    addNote = {
                    'nombre':name,
                    'nota':total,
                    'tipo':'reprobado'
                    }                
                mod.update({name:addNote})
            else:
                os.system('cls')
                print('Este estudiante aun no se encuentra vinculado a una ruta')
                os.system('pause')
        else:
            os.system('cls')
            print('primero debe asignarle un trainer a la ruta')
            os.system('pause')
    else:
        pass