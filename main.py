from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import shutil
import requests
import os

ventana = ctk.CTk() # configuracion de la ventana
ventana._set_appearance_mode("dark")  # cambia el modo de la apariencia 
ventana.title("Garras, Perros y Llaveros S.A. - Recuerdos") # asigna titulo a la ventana
ventana.geometry("1270x720")  # dimensiones de la ventana
letra_elegida = ""

#Contrato
#La función funcion_confirmar() muestra un cuadro de diálogo para seleccionar una carpeta y copia el archivo "letra.gcode" en la ruta seleccionada.
# {pre:letra_elegida ∈ {"A", "B", "C", ..., "Z", "Á", "É", "Í", "Ó", "Ú", "Ñ"}}
def funcion_confirmar():
    if letra_elegida == 'A':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraA.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraA.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Á':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraATilde.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraATilde.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'B':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraB.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraB.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'C':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraC.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraC.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'D':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraD.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraD.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'E':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraE.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraE.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'É':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraETilde.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraETilde.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'F':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraF.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraF.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'G':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraG.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraG.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'H':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraH.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraH.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'I':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraI.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraI.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Í':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraITilde.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraITilde.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'J':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraJ.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraJ.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'K':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraK.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraK.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'L':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraL.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraL.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'M':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraM.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraM.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'N':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraN.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraN.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Ñ':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraNI.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraNI.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'O':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraO.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraO.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Ó':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraOTilde.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraOTilde.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'P':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraP.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraP.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Q':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraQ.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraQ.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'R':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraR.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraR.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'S':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraS.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraS.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'T':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraT.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraT.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'U':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraU.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraU.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Ú':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraUTilde.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraUTilde.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'V':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraV.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraV.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'W':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraW.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraW.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'X':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraX.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraX.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Y':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraY.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraY.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    elif letra_elegida == 'Z':
        url = 'https://raw.githubusercontent.com/JoshuaMendez/ProyectoMora/main/pythonLetters/gcode/letraZ.gcode'
        ruta_destino = filedialog.askdirectory()
        nombre_archivo = 'letraZ.gcode'
        response = requests.get(url)
        contenido = response.text
        with open(f"{ruta_destino}/{nombre_archivo}", 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo guardado en {ruta_destino}/{nombre_archivo}")
    impresion_exitosa = ctk.CTkLabel(ventana, text="La impresión ha sido un exito  ", font=("consolas", 18, "bold"), width=400, height=10)
    impresion_exitosa.place(x=0, y=100)
    #{post:nombre_archivo ∈ {gcode}}
#Contrato
#La función funcion_confirmar() valida que letra ha sido elegida y con base a la letra elegida entraga el grafico de como se veria impresa en 3D y abre la opcion de confirmar impresión.
# usa la variable letra_elegido de tipo string , usa un boton y un label elementos de la interfaz.
#{pre:letra_elegida ∈ {"A", "B", "C", ..., "Z", "Á", "É", "Í", "Ó", "Ú", "Ñ"}}
def funcion_imprimir():
    global letra_elegida
    if letra_elegida!="":
        boton_confrimar=ctk.CTkButton(ventana, text="Confirmar", font=("arial", 18), height=50, width=200,command=funcion_confirmar)
        boton_confrimar.place(x=100,y=550)
        if letra_elegida=="A":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraA.png"), size=(300, 300))
        if letra_elegida=="B":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraB.png"), size=(300, 300))
        if letra_elegida=="C":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraC.png"), size=(300, 300))
        if letra_elegida=="D":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraD.png"), size=(300, 300))
        if letra_elegida=="E":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraE.png"), size=(300, 300))
        if letra_elegida=="F":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraF.png"), size=(300, 300))
        if letra_elegida=="G":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraG.png"), size=(300, 300))
        if letra_elegida=="H":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraH.png"), size=(300, 300))
        if letra_elegida=="I":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraI.png"), size=(300, 300))
        if letra_elegida=="J":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraJ.png"), size=(300, 300))
        if letra_elegida=="K":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraK.png"), size=(300, 300))
        if letra_elegida=="L":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraL.png"), size=(300, 300))
        if letra_elegida=="M":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraM.png"), size=(300, 300))
        if letra_elegida=="N":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraN.png"), size=(300, 300))
        if letra_elegida=="O":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraO.png"), size=(300, 300))
        if letra_elegida=="P":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraP.png"), size=(300, 300))
        if letra_elegida=="Q":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraQ.png"), size=(300, 300))
        if letra_elegida=="R":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraR.png"), size=(300, 300))
        if letra_elegida=="S":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraS.png"), size=(300, 300))
        if letra_elegida=="T":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraT.png"), size=(300, 300))
        if letra_elegida=="U":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraU.png"), size=(300, 300))
        if letra_elegida=="V":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraV.png"), size=(300, 300))
        if letra_elegida=="W":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraW.png"), size=(300, 300))
        if letra_elegida=="X":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraX.png"), size=(300, 300))
        if letra_elegida=="Y":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraY.png"), size=(300, 300))
        if letra_elegida=="Z":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraZ.png"), size=(300, 300))
        if letra_elegida=="Ñ":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraNI.png"), size=(300, 300))
        if letra_elegida=="Á":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraATilde.png"), size=(300, 300))
        if letra_elegida=="É":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraETilde.png"), size=(300, 300))
        if letra_elegida=="Í":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraITilde.png"), size=(300, 300))
        if letra_elegida=="Ó":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraOTilde.png"), size=(300, 300))
        if letra_elegida=="Ú":
            img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\pythonLetters\screenshots\letraUTilde.png"), size=(300, 300))
        grafico=ctk.CTkLabel(ventana,text="",image=img, height=300, width=300)
        grafico.place(x=100,y=200)
    else:
         return False
    #{post:img ∈ {screenshots}
  #Sebastian Izquierdo S.
  # Contrato
# La función funcion_aceptar() recibe una nueva letra ingresada, la valida y actualiza la letra elegida.
# Utiliza las variables globales nuevaLetra y letra_elegida y son de tipo string.
# Interfaz: entrada_letranueva (campo de entrada de texto), mensaje_error (etiqueta para mostrar mensajes de error), letra_seleccionada (etiqueta que muestra la letra seleccionada).
# Retorna False si la nueva letra no es válida.
# {pre:len(nuevaletra)>0 and len(nuevaletra)<0}
def funcion_aceptar():
    global nuevaLetra, letra_elegida

    # Obtener la nueva letra ingresada
    nuevaLetra = entrada_letranueva.get()

    # Reiniciar el mensaje de error
    mensaje_error = ctk.CTkLabel(ventana, text="", font=("consolas", 18, "bold"))
    mensaje_error.place(x=500, y=550)
    mensaje_error.configure(text="")

    # Validar la nueva letra
    if nuevaLetra.isdigit():
        mensaje_error.configure(text="¡Eso no parece una letra!                  ")
        return False
    if len(nuevaLetra) > 1 or len(nuevaLetra) == 0:
        mensaje_error.configure(text="¡Recuerda que las letras tienen 1 caracter!")
        print('es más de un caracter')
        return False
    else:
        print('correcto')
        letra_elegida = nuevaLetra.upper()
        mensaje_error.configure(text="Se cambió exitosamente                      ")
        letra_seleccionada.configure(text="Letra seleccionada: " + str(letra_elegida))
    #{post:letra_seleccionada = letra_elegida}
    # Sebastian Izquierdo S.
# Contrato
# La función cambiarletra() muestra la interfaz para cambiar la letra seleccionada.
# Utiliza las variables globales letra_elegida, entrada_letranueva, aceptar, letra_seleccionada y cambiarletraboton.
# Interfaz: Ingrese_letranueva (etiqueta para indicar que se ingrese la nueva letra).
#{pre: oprimir boton cambiar letra}
def cambiarletra():
    global letra_elegida, entrada_letranueva, aceptar, letra_seleccionada, cambiarletraboton

    # Interfaz cambiar letra
    Ingrese_letranueva = ctk.CTkLabel(ventana, text="Ingrese la letra:  ", font=("consolas", 18, "bold"), width=400, height=10)
    Ingrese_letranueva.place(x=400, y=400)
    entrada_letranueva = ctk.CTkEntry(ventana, font=("consolas", 12, "bold"), width=100, height=50)
    entrada_letranueva.place(x=500, y=450)
    aceptar = ctk.CTkButton(ventana, text="Aceptar", font=("arial", 18), height=50, width=200, command=funcion_aceptar)
    aceptar.place(x=700, y=450)
    cambiarletraboton.place_forget()
#{post:aceptar = interfaz letranueva}
# Sebastian Izquierdo S.

    #Contrato
    #La función algoritmo_sugerencia() analiza el texto ingresado y sugiere la letra más repetida como recordatorio.
    #Utiliza las variables globales letra_elegida, letra_seleccionada, cambiarletraboton, imprimir y cantidad_repeticionL.
    #Interfaz: Etiqueta que muestra el resultado de la sugerencia.
    #{pre: valor diccionario de las letras>0}
def algoritmo_sugerencia():
    global letra_elegida, letra_seleccionada, cambiarletraboton, imprimir, cantidad_repeticionL
    texto = entrada_texto.get()
    texto = texto.upper()
    cantidad_repeticionL = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
                            "M": 0, "N": 0,"Ñ":0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0,"":0,"Á":0,"É":0,"Í":0,"Ó":0,"Ú":0}
    i = 0
    while i < len(texto):
        if texto[i] in cantidad_repeticionL:
            cantidad_repeticionL[texto[i]] += 1
        i += 1
    letra_masrepetida = max(cantidad_repeticionL, key=cantidad_repeticionL.get)
    r = ("Te sugiero la letra "+str(letra_masrepetida)+" para tu recordatorio.")
    if cantidad_repeticionL[letra_masrepetida] == 0:
        r = "No hay letras"
        letra_masrepetida= ""
    if cantidad_repeticionL[letra_masrepetida] == 1:
        R = texto[0]
    resultado.configure(text=r)
    letra_elegida = letra_masrepetida
    letra_seleccionada = ctk.CTkLabel(ventana, text="Letra seleccionada: "+str(letra_elegida), font=("consolas", 20, "bold"))
    letra_seleccionada.place(x=500, y=300)
    cambiarletraboton = ctk.CTkButton(ventana, text="Cambiar letra", font=(
        "arial", 18), height=50, width=200, command=cambiarletra)
    cambiarletraboton.place(x=500, y=340)
    imprimir = ctk.CTkButton(ventana, text="Imprimir", font=("arial", 18), height=50, width=200,command=funcion_imprimir)
    imprimir.place(x=800, y=340)
    #{post:valor de letra_sugerida >= valor otras letras}
    #Sebastian Izquierdo S.


# elementos de la ventana principal

# Título de la ventana
Titulo = ctk.CTkLabel(
    ventana, text="Garras, Perros y Llaveros S.A.", font=("consolas", 25, "bold"))
Titulo.place(x=340, y=30)

# Etiqueta para ingresar texto
Ingrese_texto = ctk.CTkLabel(ventana, text="Ingrese las palabras , frases o poemas de su preferencia: ", font=(
    "consolas", 18, "bold"), width=400, height=10)
Ingrese_texto.place(x=500, y=100)
# Campo de entrada de texto
entrada_texto = ctk.CTkEntry(ventana, font=(
    "consolas", 12, "bold"), width=550, height=50)
entrada_texto.place(x=500, y=150)
# Etiqueta para mostrar el resultado
resultado = ctk.CTkLabel(ventana, text="", font=("consolas", 14, "bold"))
# Botón para enviar el texto y ejecutar el algoritmo de sugerencia
Enviar = ctk.CTkButton(ventana, text="Enviar", font=(
    "arial", 18), command=algoritmo_sugerencia, height=50, width=200)
Enviar.place(x=500, y=230)
resultado.place(x=710, y=230)

# Iniciar la ventana principal
ventana.mainloop()
