import os
def MainMenu():
    lstOp = (1,2,3,4,5,6,7)
    titulo = '''
    ****************************
    * BIENVENIDO A CAMPUSLANDS *
    ****************************
    '''
    opciones = '1. Gestión campers\n2. Trainers\n3. Rutas\n4. Gestionar Exámenes\n5. Consultar campers en riesgo\n6. Reportes\n7. Salir'
    os.system('cls')
    try:
        print(titulo)
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MainMenu()
    except ValueError:
        return MainMenu()
    else:
        return n

def MenuTrainers():
    lstOp = (1,2,3)
    opciones = '1. Agregar trainer\n2. Asignar salon y rutas\n3. Salir'
    os.system('cls')
    try:
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuTrainers()
    except ValueError:
        return MenuTrainers()
    else:
        return n
    
def MenuCampers():
    lstOp = (1,2,3)
    opciones = '1. Añadir Camper\n2. Asignar ruta a camper\n3. Salir'
    os.system('cls')
    try:
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuCampers()
    except ValueError:
        return MenuCampers()
    else:
        return n

def MenuSalones():
    lstOp = (1,2,3)
    opciones = '1. Apolo\n2. Sputnik\n3. Artemis'
    os.system('cls')
    try:
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuSalones()
    except ValueError:
        return MenuSalones()
    else:
        return n

def MenuRutas():
    lstOp = (1,2,3)
    opciones = '1. Java\n2. NodeJs\n3. NetCore'
    os.system('cls')
    try:
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuRutas()
    except ValueError:
        return MenuRutas()
    else:
        return n

def MenuExams():
    lstOp = (1,2,3)
    opciones = '1. prueba de ingreso\n2. Exámen de modúlo\n3. Salir'
    os.system('cls')
    try:
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuExams()
    except ValueError:
        return MenuExams()
    else:
        return n

def MenuModulos():
    lstOp = (1,2,3,4,5)
    opciones = '1. Fundamentos\n2. Programación Web\n3. Programación Formal\n4. Bases de datos\n5. backend'
    os.system('cls')
    try:
        print('Ingrese a que modulo desea agregar las notas:')
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuExams()
    except ValueError:
        return MenuExams()
    else:
        return n

def MenuReps():
    lstOp = (1,2,3,4,5,6,7)
    opciones = '1. Campers inscritos\n2. Campers aprobados\n3. Lista de trainers\n4. Estudiantes con bajo rendimiento\n5. Ver campers y trainer por ruta\n6. Campers aprobados y reprobados por modulo\n7. Salir'
    os.system('cls')
    try:
        print('Ingrese a que modulo desea agregar las notas:')
        print(opciones)
        n = int(input(')..'))
        if (n not in lstOp):
            print('Digito ingresado inválido')
            os.system('pause')
            return MenuReps()
    except ValueError:
        return MenuReps()
    else:
        return n