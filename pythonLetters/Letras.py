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

# Letra B
urlLetraB = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraB.txt"
textoLetraB = requests.get(urlLetraB)
printearLetraB = textoLetraB.text

# Letra C
urlLetraC = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraC.txt"
textoLetraC = requests.get(urlLetraC)
printearLetraC = textoLetraC.text

# Letra D
urlLetraD = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraD.txt"
textoLetraD = requests.get(urlLetraD)
printearLetraD = textoLetraD.text

# Letra E
urlLetraE = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraE.txt"
textoLetraE = requests.get(urlLetraE)
printearLetraE = textoLetraE.text

# Letra F
urlLetraF = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraF.txt"
textoLetraF = requests.get(urlLetraF)
printearLetraF = textoLetraF.text

# Letra G
urlLetraG = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraG.txt"
textoLetraG = requests.get(urlLetraG)
printearLetraG = textoLetraG.text

# Letra H
urlLetraH = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraH.txt"
textoLetraH = requests.get(urlLetraH)
printearLetraH = textoLetraH.text

# Letra I
urlLetraI = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraI.txt"
textoLetraI = requests.get(urlLetraI)
printearLetraI = textoLetraI.text

# Letra J
urlLetraJ = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraJ.txt"
textoLetraJ = requests.get(urlLetraJ)
printearLetraJ = textoLetraJ.text

# Letra K
urlLetraK = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraK.txt"
textoLetraK = requests.get(urlLetraK)
printearLetraK = textoLetraK.text

# Letra L
urlLetraL = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraL.txt"
textoLetraL = requests.get(urlLetraL)
printearLetraL = textoLetraL.text

# Letra M
urlLetraM = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraM.txt"
textoLetraM = requests.get(urlLetraM)
printearLetraM = textoLetraM.text

# Letra N
urlLetraN = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraN.txt"
textoLetraN = requests.get(urlLetraN)
printearLetraN = textoLetraN.text

# Letra NI - Ñ
urlLetraNI = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraNI.txt"
textoLetraNI = requests.get(urlLetraNI)
printearLetraNI = textoLetraNI.text

# Letra O
urlLetraO = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraO.txt"
textoLetraO = requests.get(urlLetraO)
printearLetraO = textoLetraO.text

# Letra P
urlLetraP = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraP.txt"
textoLetraP = requests.get(urlLetraP)
printearLetraP = textoLetraP.text

# Letra Q
urlLetraQ = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraQ.txt"
textoLetraQ = requests.get(urlLetraQ)
printearLetraQ = textoLetraQ.text

# Letra R
urlLetraR = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraR.txt"
textoLetraR = requests.get(urlLetraR)
printearLetraR = textoLetraR.text

# Letra S
urlLetraS = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraS.txt"
textoLetraS = requests.get(urlLetraS)
printearLetraS = textoLetraS.text

# Letra T
urlLetraT = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraT.txt"
textoLetraT = requests.get(urlLetraT)
printearLetraT = textoLetraT.text

# Letra U
urlLetraU = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraU.txt"
textoLetraU = requests.get(urlLetraU)
printearLetraU = textoLetraU.text

# Letra V
urlLetraV = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraV.txt"
textoLetraV = requests.get(urlLetraV)
printearLetraV = textoLetraV.text

# Letra W
urlLetraW = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraW.txt"
textoLetraW = requests.get(urlLetraW)
printearLetraW = textoLetraW.text

# Letra X
urlLetraX = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraX.txt"
textoLetraX = requests.get(urlLetraX)
printearLetraX = textoLetraX.text

# Letra Y
urlLetraY = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraY.txt"
textoLetraY = requests.get(urlLetraY)
printearLetraY = textoLetraY.text

# Letra Z
urlLetraZ = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraZ.txt"
textoLetraZ = requests.get(urlLetraZ)
printearLetraZ = textoLetraZ.text

# Letra A Tilde
urlLetraATilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraATilde.txt"
textoLetraATilde = requests.get(urlLetraATilde)
printearLetraATilde = textoLetraATilde.text

# Letra E Tilde
urlLetraETilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraETilde.txt"
textoLetraETilde = requests.get(urlLetraETilde)
printearLetraETilde = textoLetraETilde.text

# Letra I Tilde
urlLetraITilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraITilde.txt"
textoLetraITilde = requests.get(urlLetraITilde)
printearLetraITilde = textoLetraITilde.text

# Letra O Tilde
urlLetraOTilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraOTilde.txt"
textoLetraOTilde = requests.get(urlLetraOTilde)
printearLetraOTilde = textoLetraOTilde.text

# Letra U Tilde
urlLetraUTilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/LetraUTilde.txt"
textoLetraUTilde = requests.get(urlLetraUTilde)
printearLetraUTilde = textoLetraUTilde.text

def llamarLetras():
    pregunta = input('¿Qué Letra quieres imprimir?: ')
    pregunta = pregunta.upper()
    if pregunta == 'A':
        cargandoLetras()
        print(printearLetraA)
    elif pregunta == 'B':
        cargandoLetras()
        print(printearLetraB)
    elif pregunta == 'C':
        cargandoLetras()
        print(printearLetraC)
    elif pregunta == 'D':
        cargandoLetras()
        print(printearLetraD)
    elif pregunta == 'E':
        cargandoLetras()
        print(printearLetraE)
    elif pregunta == 'F':
        cargandoLetras()
        print(printearLetraF)
    elif pregunta == 'G':
        cargandoLetras()
        print(printearLetraG)
    elif pregunta == 'H':
        cargandoLetras()
        print(printearLetraH)
    elif pregunta == 'I':
        cargandoLetras()
        print(printearLetraI)
    elif pregunta == 'J':
        cargandoLetras()
        print(printearLetraJ)
    elif pregunta == 'K':
        cargandoLetras()
        print(printearLetraK)
    elif pregunta == 'L':
        cargandoLetras()
        print(printearLetraL)
    elif pregunta == 'M':
        cargandoLetras()
        print(printearLetraM)
    elif pregunta == 'N':
        cargandoLetras()
        print(printearLetraN)
    elif pregunta == 'Ñ':
        cargandoLetras()
        print(printearLetraNI)
    elif pregunta == 'O':
        cargandoLetras()
        print(printearLetraO)
    elif pregunta == 'P':
        cargandoLetras()
        print(printearLetraP)
    elif pregunta == 'Q':
        cargandoLetras()
        print(printearLetraQ)
    elif pregunta == 'R':
        cargandoLetras()
        print(printearLetraR)
    elif pregunta == 'S':
        cargandoLetras()
        print(printearLetraS)
    elif pregunta == 'T':
        cargandoLetras()
        print(printearLetraT)
    elif pregunta == 'U':
        cargandoLetras()
        print(printearLetraU)
    elif pregunta == 'V':
        cargandoLetras()
        print(printearLetraV)
    elif pregunta == 'W':
        cargandoLetras()
        print(printearLetraW)
    elif pregunta == 'X':
        cargandoLetras()
        print(printearLetraX)
    elif pregunta == 'Y':
        cargandoLetras()
        print(printearLetraY)
    elif pregunta == 'Z':
        cargandoLetras()
        print(printearLetraZ)



llamarLetras()