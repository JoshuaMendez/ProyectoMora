import requests
import time
import random
import string
lista = []
i = 0
while i <= 3:
    for i in range(10):
        elemento = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        lista.append(elemento)
    i += 1

def thing_not_complete():
    print('Hola')
animation = "|/-\\"
idx = 0
while thing_not_complete():
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)

def cargandoLetras():
    print('')
    print('cargando letra...')
    print('')
    time.sleep(0.5)
    print('')
    print('...')
    print('')
    time.sleep(0.5)
    print('')
    print('..')
    print('')
    time.sleep(0.5)
    print('')
    print('.')
    print('')
    time.sleep(0.5)
    print('')
    print('creando código...')
    print('')
    time.sleep(0.5)
    print('')
    print(lista[0])
    print('')
    time.sleep(0.5)
    print('')
    print(lista[1])
    print('')
    time.sleep(0.5)
    print('')
    print(lista[2])
    print('')
    time.sleep(0.5)
    print('')
    print(lista[3])
    print('')
    time.sleep(0.5)
    print('')
    print('empaquetando...')
    print('')
    time.sleep(0.5)
    print('')
    print('...')
    print('')
    time.sleep(0.5)
    print('')
    print('..')
    print('')
    time.sleep(0.5)
    print('')
    print('.')
    print('')
    time.sleep(0.5)
    print('')

# Letra A
urlLetraA = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraA.txt"
textoLetraA = requests.get(urlLetraA)
printearLetraA = textoLetraA.text

# Letra B
urlLetraB = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraB.txt"
textoLetraB = requests.get(urlLetraB)
printearLetraB = textoLetraB.text

# Letra C
urlLetraC = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraC.txt"
textoLetraC = requests.get(urlLetraC)
printearLetraC = textoLetraC.text

# Letra D
urlLetraD = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraD.txt"
textoLetraD = requests.get(urlLetraD)
printearLetraD = textoLetraD.text

# Letra E
urlLetraE = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraE.txt"
textoLetraE = requests.get(urlLetraE)
printearLetraE = textoLetraE.text

# Letra F
urlLetraF = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraF.txt"
textoLetraF = requests.get(urlLetraF)
printearLetraF = textoLetraF.text

# Letra G
urlLetraG = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraG.txt"
textoLetraG = requests.get(urlLetraG)
printearLetraG = textoLetraG.text

# Letra H
urlLetraH = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraH.txt"
textoLetraH = requests.get(urlLetraH)
printearLetraH = textoLetraH.text

# Letra I
urlLetraI = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraI.txt"
textoLetraI = requests.get(urlLetraI)
printearLetraI = textoLetraI.text

# Letra J
urlLetraJ = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraJ.txt"
textoLetraJ = requests.get(urlLetraJ)
printearLetraJ = textoLetraJ.text

# Letra K
urlLetraK = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraK.txt"
textoLetraK = requests.get(urlLetraK)
printearLetraK = textoLetraK.text

# Letra L
urlLetraL = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraL.txt"
textoLetraL = requests.get(urlLetraL)
printearLetraL = textoLetraL.text

# Letra M
urlLetraM = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraM.txt"
textoLetraM = requests.get(urlLetraM)
printearLetraM = textoLetraM.text

# Letra N
urlLetraN = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraN.txt"
textoLetraN = requests.get(urlLetraN)
printearLetraN = textoLetraN.text

# Letra NI - Ñ
urlLetraNI = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraNI.txt"
textoLetraNI = requests.get(urlLetraNI)
printearLetraNI = textoLetraNI.text

# Letra O
urlLetraO = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraO.txt"
textoLetraO = requests.get(urlLetraO)
printearLetraO = textoLetraO.text

# Letra P
urlLetraP = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraP.txt"
textoLetraP = requests.get(urlLetraP)
printearLetraP = textoLetraP.text

# Letra Q
urlLetraQ = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraQ.txt"
textoLetraQ = requests.get(urlLetraQ)
printearLetraQ = textoLetraQ.text

# Letra R
urlLetraR = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraR.txt"
textoLetraR = requests.get(urlLetraR)
printearLetraR = textoLetraR.text

# Letra S
urlLetraS = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraS.txt"
textoLetraS = requests.get(urlLetraS)
printearLetraS = textoLetraS.text

# Letra T
urlLetraT = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraT.txt"
textoLetraT = requests.get(urlLetraT)
printearLetraT = textoLetraT.text

# Letra U
urlLetraU = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraU.txt"
textoLetraU = requests.get(urlLetraU)
printearLetraU = textoLetraU.text

# Letra V
urlLetraV = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraV.txt"
textoLetraV = requests.get(urlLetraV)
printearLetraV = textoLetraV.text

# Letra W
urlLetraW = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraW.txt"
textoLetraW = requests.get(urlLetraW)
printearLetraW = textoLetraW.text

# Letra X
urlLetraX = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraX.txt"
textoLetraX = requests.get(urlLetraX)
printearLetraX = textoLetraX.text

# Letra Y
urlLetraY = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraY.txt"
textoLetraY = requests.get(urlLetraY)
printearLetraY = textoLetraY.text

# Letra Z
urlLetraZ = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraZ.txt"
textoLetraZ = requests.get(urlLetraZ)
printearLetraZ = textoLetraZ.text

# Letra A Tilde
urlLetraATilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraATilde.txt"
textoLetraATilde = requests.get(urlLetraATilde)
printearLetraATilde = textoLetraATilde.text

# Letra E Tilde
urlLetraETilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraETilde.txt"
textoLetraETilde = requests.get(urlLetraETilde)
printearLetraETilde = textoLetraETilde.text

# Letra I Tilde
urlLetraITilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraITilde.txt"
textoLetraITilde = requests.get(urlLetraITilde)
printearLetraITilde = textoLetraITilde.text

# Letra O Tilde
urlLetraOTilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraOTilde.txt"
textoLetraOTilde = requests.get(urlLetraOTilde)
printearLetraOTilde = textoLetraOTilde.text

# Letra U Tilde
urlLetraUTilde = "https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/txt/letraUTilde.txt"
textoLetraUTilde = requests.get(urlLetraUTilde)
printearLetraUTilde = textoLetraUTilde.text

def llamarLetras():
    pregunta = input('¿Qué Letra quieres imprimir?: ')
    pregunta = pregunta.upper()
    if pregunta == 'A':
        cargandoLetras()
        print(printearLetraA)
        repetir()
    elif pregunta == 'B':
        cargandoLetras()
        print(printearLetraB)
        repetir()
    elif pregunta == 'C':
        cargandoLetras()
        print(printearLetraC)
        repetir()
    elif pregunta == 'D':
        cargandoLetras()
        print(printearLetraD)
        repetir()
    elif pregunta == 'E':
        cargandoLetras()
        print(printearLetraE)
        repetir()
    elif pregunta == 'F':
        cargandoLetras()
        print(printearLetraF)
        repetir()
    elif pregunta == 'G':
        cargandoLetras()
        print(printearLetraG)
        repetir()
    elif pregunta == 'H':
        cargandoLetras()
        print(printearLetraH)
        repetir()
    elif pregunta == 'I':
        cargandoLetras()
        print(printearLetraI)
        repetir()
    elif pregunta == 'J':
        cargandoLetras()
        print(printearLetraJ)
        repetir()
    elif pregunta == 'K':
        cargandoLetras()
        print(printearLetraK)
        repetir()
    elif pregunta == 'L':
        cargandoLetras()
        print(printearLetraL)
        repetir()
    elif pregunta == 'M':
        cargandoLetras()
        print(printearLetraM)
        repetir()
    elif pregunta == 'N':
        cargandoLetras()
        print(printearLetraN)
        repetir()
    elif pregunta == 'Ñ':
        cargandoLetras()
        print(printearLetraNI)
        repetir()
    elif pregunta == 'O':
        cargandoLetras()
        print(printearLetraO)
        repetir()
    elif pregunta == 'P':
        cargandoLetras()
        print(printearLetraP)
        repetir()
    elif pregunta == 'Q':
        cargandoLetras()
        print(printearLetraQ)
        repetir()
    elif pregunta == 'R':
        cargandoLetras()
        print(printearLetraR)
        repetir()
    elif pregunta == 'S':
        cargandoLetras()
        print(printearLetraS)
        repetir()
    elif pregunta == 'T':
        cargandoLetras()
        print(printearLetraT)
        repetir()
    elif pregunta == 'U':
        cargandoLetras()
        print(printearLetraU)
        repetir()
    elif pregunta == 'V':
        cargandoLetras()
        print(printearLetraV)
        repetir()
    elif pregunta == 'W':
        cargandoLetras()
        print(printearLetraW)
        repetir()
    elif pregunta == 'X':
        cargandoLetras()
        print(printearLetraX)
        repetir()
    elif pregunta == 'Y':
        cargandoLetras()
        print(printearLetraY)
        repetir()
    elif pregunta == 'Z':
        cargandoLetras()
        print(printearLetraZ)
        repetir()
    elif pregunta == 'Á':
        cargandoLetras()
        print(printearLetraATilde)
        repetir()
    elif pregunta == 'É':
        cargandoLetras()
        print(printearLetraETilde)
        repetir()
    elif pregunta == 'Í':
        cargandoLetras()
        print(printearLetraITilde)
        repetir()
    elif pregunta == 'Ó':
        cargandoLetras()
        print(printearLetraOTilde)
        repetir()
    elif pregunta == 'Ú':
        cargandoLetras()
        print(printearLetraUTilde)
        repetir()

def repetir():
    repetidera = input('¿Quieres imprimir otra letra? Sí/No ')
    repetidera = repetidera.upper()
    if repetidera == 'SI' or repetidera == 'SÍ':
        llamarLetras()
    elif repetidera == 'NO':
        print('Muchas gracias por usar nuestros servicios. ¡Adios!')
        raise SystemExit
