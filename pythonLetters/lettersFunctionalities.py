import requests
import time
import random
import string
import webbrowser
import os

def limpiar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y macOS
        os.system('clear')

lista = []
i = 0
while i <= 3:
    for i in range(10):
        elemento = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        lista.append(elemento)
    i += 1


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
    global pregunta
    pregunta = input('¿Qué Letra quieres imprimir?: ')
    pregunta = pregunta.upper()
    if pregunta == 'A':
        cargandoLetras()
        print(printearLetraA)
        guardar()
        repetir()
    elif pregunta == 'B':
        cargandoLetras()
        print(printearLetraB)
        guardar()
        repetir()
    elif pregunta == 'C':
        cargandoLetras()
        print(printearLetraC)
        guardar()
        repetir()
    elif pregunta == 'D':
        cargandoLetras()
        print(printearLetraD)
        guardar()
        repetir()
    elif pregunta == 'E':
        cargandoLetras()
        print(printearLetraE)
        guardar()
        repetir()
    elif pregunta == 'F':
        cargandoLetras()
        print(printearLetraF)
        guardar()
        repetir()
    elif pregunta == 'G':
        cargandoLetras()
        print(printearLetraG)
        guardar()
        repetir()
    elif pregunta == 'H':
        cargandoLetras()
        print(printearLetraH)
        guardar()
        repetir()
    elif pregunta == 'I':
        cargandoLetras()
        print(printearLetraI)
        guardar()
        repetir()
    elif pregunta == 'J':
        cargandoLetras()
        print(printearLetraJ)
        guardar()
        repetir()
    elif pregunta == 'K':
        cargandoLetras()
        print(printearLetraK)
        guardar()
        repetir()
    elif pregunta == 'L':
        cargandoLetras()
        print(printearLetraL)
        guardar()
        repetir()
    elif pregunta == 'M':
        cargandoLetras()
        print(printearLetraM)
        guardar()
        repetir()
    elif pregunta == 'N':
        cargandoLetras()
        print(printearLetraN)
        guardar()
        repetir()
    elif pregunta == 'Ñ':
        cargandoLetras()
        print(printearLetraNI)
        guardar()
        repetir()
    elif pregunta == 'O':
        cargandoLetras()
        print(printearLetraO)
        guardar()
        repetir()
    elif pregunta == 'P':
        cargandoLetras()
        print(printearLetraP)
        guardar()
        repetir()
    elif pregunta == 'Q':
        cargandoLetras()
        print(printearLetraQ)
        guardar()
        repetir()
    elif pregunta == 'R':
        cargandoLetras()
        print(printearLetraR)
        guardar()
        repetir()
    elif pregunta == 'S':
        cargandoLetras()
        print(printearLetraS)
        guardar()
        repetir()
    elif pregunta == 'T':
        cargandoLetras()
        print(printearLetraT)
        guardar()
        repetir()
    elif pregunta == 'U':
        cargandoLetras()
        print(printearLetraU)
        guardar()
        repetir()
    elif pregunta == 'V':
        cargandoLetras()
        print(printearLetraV)
        guardar()
        repetir()
    elif pregunta == 'W':
        cargandoLetras()
        print(printearLetraW)
        guardar()
        repetir()
    elif pregunta == 'X':
        cargandoLetras()
        print(printearLetraX)
        guardar()
        repetir()
    elif pregunta == 'Y':
        cargandoLetras()
        print(printearLetraY)
        guardar()
        repetir()
    elif pregunta == 'Z':
        cargandoLetras()
        print(printearLetraZ)
        guardar()
        repetir()
    elif pregunta == 'Á':
        cargandoLetras()
        print(printearLetraATilde)
        guardar()
        repetir()
    elif pregunta == 'É':
        cargandoLetras()
        print(printearLetraETilde)
        guardar()
        repetir()
    elif pregunta == 'Í':
        cargandoLetras()
        print(printearLetraITilde)
        guardar()
        repetir()
    elif pregunta == 'Ó':
        cargandoLetras()
        print(printearLetraOTilde)
        guardar()
        repetir()
    elif pregunta == 'Ú':
        cargandoLetras()
        print(printearLetraUTilde)
        guardar()
        repetir()

def guardar():
    guardadera = input(f'¿Quieres guardar el archivo de la letra {pregunta}? Sí/No ')
    guardadera = guardadera.upper()
    if guardadera == 'SÍ' or guardadera == 'SI':
        if pregunta == 'A':
            respuesta_archivo = requests.get(urlLetraA)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "letraA.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'B':
            respuesta_archivo = requests.get(urlLetraB)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraB.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'C':
            respuesta_archivo = requests.get(urlLetraC)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraC.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'D':
            respuesta_archivo = requests.get(urlLetraD)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraD.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'E':
            respuesta_archivo = requests.get(urlLetraE)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraE.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'F':
            respuesta_archivo = requests.get(urlLetraF)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraF.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'G':
            respuesta_archivo = requests.get(urlLetraG)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraG.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'H':
            respuesta_archivo = requests.get(urlLetraH)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraH.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'I':
            respuesta_archivo = requests.get(urlLetraI)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraI.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'J':
            respuesta_archivo = requests.get(urlLetraJ)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraJ.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'K':
            respuesta_archivo = requests.get(urlLetraK)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraK.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'L':
            respuesta_archivo = requests.get(urlLetraL)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraL.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'M':
            respuesta_archivo = requests.get(urlLetraM)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraM.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'N':
            respuesta_archivo = requests.get(urlLetraN)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraN.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Ñ':
            respuesta_archivo = requests.get(urlLetraNI)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraNI.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'O':
            respuesta_archivo = requests.get(urlLetraO)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraO.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'P':
            respuesta_archivo = requests.get(urlLetraP)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraP.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Q':
            respuesta_archivo = requests.get(urlLetraQ)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraQ.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'R':
            respuesta_archivo = requests.get(urlLetraR)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraR.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'S':
            respuesta_archivo = requests.get(urlLetraS)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraS.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'T':
            respuesta_archivo = requests.get(urlLetraT)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraT.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'U':
            respuesta_archivo = requests.get(urlLetraU)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraU.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'V':
            respuesta_archivo = requests.get(urlLetraV)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraV.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'W':
            respuesta_archivo = requests.get(urlLetraW)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraW.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'X':
            respuesta_archivo = requests.get(urlLetraX)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraX.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Y':
            respuesta_archivo = requests.get(urlLetraY)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraY.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Z':
            respuesta_archivo = requests.get(urlLetraZ)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraZ.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Á':
            respuesta_archivo = requests.get(urlLetraATilde)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraATilde.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'É':
            respuesta_archivo = requests.get(urlLetraETilde)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraETilde.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Í':
            respuesta_archivo = requests.get(urlLetraITilde)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraITilde.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Ó':
            respuesta_archivo = requests.get(urlLetraOTilde)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraOTilde.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')
        elif pregunta == 'Ú':
            respuesta_archivo = requests.get(urlLetraUTilde)
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            ruta_archivo_gcode = os.path.join(carpeta_descargas, "LetraUTilde.gcode")
            with open(ruta_archivo_gcode, "w") as archivo_gcode:
                archivo_gcode.write(respuesta_archivo.text)
            print(f'La letra {pregunta} se guardó correctamente en /Descargas/')


    elif guardadera == 'NO':
        print(f'No guardaremos la letra {pregunta} en tu dispositivo.')
        repetir()
    else:
        print('Error en la respuesta...')
        time.sleep(1)
        print('Repitiendo procesos...')
        llamarLetras()

def repetir():
    repetidera = input('¿Quieres imprimir otra letra? Sí/No ')
    repetidera = repetidera.upper()
    if repetidera == 'SI' or repetidera == 'SÍ':
        limpiar_terminal()
        llamarLetras()
    else:
        print('Muchas gracias por usar nuestros servicios. ¡Adios!')
        time.sleep(1)
        limpiar_terminal()
        raise SystemExit