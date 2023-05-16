from lettersFunctions import *
import requests
import time

ExteriorListaX = [100, 120, 120, 115, 115, 105, 105, 100, 100]
ExteriorListaY = [150, 150, 110, 110, 130, 130, 110, 110, 150]
InteriorListaX = []
InteriorListaY = []

#Especificaciones impresora
#Contorno Exterior

ExteriorPosX = 0
ExteriorPosY = 0
DiferenciaExterior = 0
PosZ = 0.25
E = 0

while ExteriorPosX < len(ExteriorListaX) and ExteriorPosY < len(ExteriorListaY): 

    if DiferenciaExterior < (len(ExteriorListaX)) and DiferenciaExterior < (len(ExteriorListaY)) and (DiferenciaExterior != len(ExteriorListaX ) - 1):

        DiferenciaExterior = DiferenciaExterior + 1

        E1 = abs(int(ExteriorListaX[ExteriorPosX]) - int(ExteriorListaX[DiferenciaExterior]))
        E2 = abs(int(ExteriorListaY[ExteriorPosY]) - int(ExteriorListaY[DiferenciaExterior]))

        if E1 != 0 and E2 == 0:
            RE = E1 * 0.03
        if E2 != 0 and E1 == 0:
            RE = E2 * 0.03

        E = E + RE 
        E = round(E, 3)

    if ExteriorPosX == 0 and ExteriorPosY == 0:
        ExteriorListaX
    
    if ExteriorPosX > 1 and ExteriorPosY > 1 and ExteriorPosX < (len(ExteriorListaX) - 1) and ExteriorPosY < (len(ExteriorListaY) - 1):
        ExteriorListaX

    if DiferenciaExterior == (len(ExteriorListaX) - 1):

        E1 = abs(int(ExteriorListaX[-1]) - int(ExteriorListaX[0]))
        E2 = abs(int(ExteriorListaY[-1]) - int(ExteriorListaY[0]))

        if E1 != 0 and E2 == 0:
            RE = E1 * 0.03
        if E2 != 0 and E1 == 0:
            RE = E2 * 0.03

        E = E + RE 
        E = round(E, 3)


    ExteriorPosX = ExteriorPosX + 1
    ExteriorPosY = ExteriorPosY + 1

#Contorno Interior

InteriorPosX = 0
InteriorPosY = 0
DiferenciaInterior = 0

while InteriorPosX < len(ExteriorListaX) and InteriorPosY < len(ExteriorListaY):

    if ExteriorListaX[InteriorPosX] - 0.3 < 100:
        ValorInterior = ExteriorListaX[InteriorPosX] + 0.3
        InteriorListaX.append(ValorInterior)
    
    else:
    
        if ExteriorListaX[InteriorPosX] + 0.3 > 120:
            ValorInterior = ExteriorListaX[InteriorPosX] - 0.3
            InteriorListaX.append(ValorInterior)

        else:

            if ExteriorListaX[InteriorPosX] - 0.3 < 110:
                ValorInterior = ExteriorListaX[InteriorPosX] + 0.3
                InteriorListaX.append(ValorInterior)

            else:

                if ExteriorListaX[InteriorPosX] + 0.3 > 110:
                    ValorInterior = ExteriorListaX[InteriorPosX] - 0.3
                    InteriorListaX.append(ValorInterior)

    #Contorno interior Y

    if ExteriorListaY[InteriorPosY] + 0.3 > 150:
        ValorInterior = ExteriorListaY[InteriorPosY] - 0.3
        InteriorListaY.append(ValorInterior)
    
    else:
    
        if ExteriorListaY[InteriorPosY] - 0.3 < 110:
            ValorInterior = ExteriorListaY[InteriorPosY] + 0.3
            InteriorListaY.append(ValorInterior)

        else:

            if ExteriorListaY[InteriorPosY] - 0.3 < 135:
                ValorInterior = ExteriorListaY[InteriorPosY] - 0.3
                InteriorListaY.append(ValorInterior)

            else:

                if ExteriorListaY[InteriorPosY] + 0.3 > 135:
                    ValorInterior = ExteriorListaY[InteriorPosY] + 0.3
                    InteriorListaY.append(ValorInterior)

    InteriorPosX = InteriorPosX + 1
    InteriorPosY = InteriorPosY + 1

InteriorPosX = 0
InteriorPosY = 0

while InteriorPosX < len(InteriorListaX) and InteriorPosY < len(InteriorListaY):

    if DiferenciaInterior < (len(InteriorListaX) - 1) and DiferenciaInterior < (len(InteriorListaY) - 1):

        DiferenciaInterior = DiferenciaInterior + 1

        E1 = abs(int(InteriorListaX[InteriorPosX]) - int(InteriorListaX[DiferenciaInterior]))
        E2 = abs(int(InteriorListaY[InteriorPosY]) - int(InteriorListaY[DiferenciaInterior]))

        if E1 != 0:
            E = E1 * 0.03
        else: 
            if E2 != 0:
                E = E2 * 0.03

        E = E + E
        E = round(E, 3)

    if InteriorPosX == 0 and InteriorPosY == 0:
       E
    
    if InteriorPosX > 0 and InteriorPosY > 0 and InteriorPosX < (len(InteriorListaX) - 1) and InteriorPosY < (len(InteriorListaY) - 1):
      E 

    InteriorPosX = InteriorPosX + 1
    InteriorPosY = InteriorPosY + 1

if InteriorPosX == len(InteriorListaX) and InteriorPosY == len(InteriorListaY):

        E3 = abs(int(InteriorListaX[-2]) - int(InteriorListaX[0]))
        E4 = abs(int(InteriorListaY[-2]) - int(InteriorListaY[0]))

        if E3 != 0:
            E = E3 * 0.03
        else:
            if E4 != 0:
                E = E4 * 0.03
        E = E + E
        E = round(E, 3)

#Relleno vertical 1

x = 100
e = 3003.066
while x < 120.3:
    x = x + 0.3
    e = e + (0.03 * 29.4)
x = 120.3
e = 3063.042
while x < 146.7:
    x = x + 0.3
    e = e + (0.03 * 132.4)
#Relleno vertical 3

x = 146.7
e = 3412.578
while x < 166.7:
    x = x + 0.3
    e = e + (0.03 * 29.4)

#Relleno horizontal 1

Y = 150
e = 3495.6
while Y > 120.3:
    Y = Y - 0.3
    e = e + (0.03 * 66.4)

#Relleno horizontal 2

Y = 120.3
e = 3692.808
while Y > 17.3:
    Y = Y - 0.3
    e = e + (0.03 * 27)

def cargandoLetras():
    print('')
    time.sleep(0.5)
    print('cargando letra...')
    time.sleep(0.5)
    print('creando código...')
    time.sleep(0.5)
    print('empaquetando...')
    time.sleep(0.5)
    print('')

# Letra A
urlLetraA = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraA.txt"
textoLetraA = requests.get(urlLetraA)
printearLetraA = textoLetraA.text

def llamarLetras():
    pregunta = input('¿Qué Letra quieres imprimir?: ')
    pregunta = pregunta.upper()
    if pregunta == 'A':
        cargandoLetras()
        print(printearLetraA)
    elif pregunta == 'B':
        cargandoLetras()
        letraB()
    elif pregunta == 'C':
        cargandoLetras()
        letraC()
    elif pregunta == 'D':
        cargandoLetras()
        letraD()
    elif pregunta == 'E':
        cargandoLetras()
        letraE()
    elif pregunta == 'F':
        cargandoLetras()
        letraF()
    elif pregunta == 'G':
        cargandoLetras()
        letraG()
    elif pregunta == 'H':
        cargandoLetras()
        letraH()
    elif pregunta == 'I':
        cargandoLetras()
        letraI()
    elif pregunta == 'J':
        cargandoLetras()
        letraJ()
    elif pregunta == 'K':
        cargandoLetras()
        letraK()
    elif pregunta == 'L':
        cargandoLetras()
        letraL()
    elif pregunta == 'M':
        cargandoLetras()
        letraM()
    elif pregunta == 'N':
        cargandoLetras()
        letraN()
    elif pregunta == 'Ñ':
        cargandoLetras()
        letraNI()
    elif pregunta == 'O':
        cargandoLetras()
        letraO()
    elif pregunta == 'P':
        cargandoLetras()
        letraP()
    elif pregunta == 'Q':
        cargandoLetras()
        letraQ()
    # elif pregunta == 'R':
    #     cargandoLetras()
    #     letraR()
    elif pregunta == 'S':
        cargandoLetras()
        letraS()
    elif pregunta == 'T':
        cargandoLetras()
        letraT()
    elif pregunta == 'U':
        cargandoLetras()
        letraF()
    # elif pregunta == 'V':
    #     cargandoLetras()
    #     letraV()
    # elif pregunta == 'W':
    #     cargandoLetras()
    #     letraW()
    # elif pregunta == 'X':
    #     cargandoLetras()
    #     letraX()
    # elif pregunta == 'Y':
    #     cargandoLetras()
    #     letraY()
    # elif pregunta == 'Z':
    #     cargandoLetras()
    #     letraZ()



llamarLetras()