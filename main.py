import modules.menu as m
import modules.campers as cam
import modules.trainers as tr
import modules.rutas as rr
import modules.exams as ex
import modules.reportes as rep
if __name__=='__main__':
    campers = {}
    trainers = {}
    rutas = {
        'Java':{},
        'NodeJs':{},
        'NetCore':{}
    }
    salones = {
        'apolo':{},
        'artemis':{},
        'sputnik':{}
    }
    isActive = True
    while isActive:
        n = m.MainMenu()
        if (n == 1):
            cam.GestCampers(campers,salones)
        elif (n == 2):
            tr.GestionTr(trainers,salones,rutas)
        elif (n == 3):
            rr.nwRoute(rutas,salones)
        elif (n == 4):
            ex.GestorEx(campers,rutas)
        elif (n == 5):
            rep.Riesgo(campers)
        elif (n == 6):
            rep.Reps(campers,salones,rutas,trainers)
        elif (n == 7):
            m.os.system('cls')
            print('Hasta luego')
            m.os.system('pause')
            isActive = False