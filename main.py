import tkinter as tk
import customtkinter as ctk
ventana = ctk.CTk()
#configuracion de la ventana
ventana._set_appearance_mode("dark")#cambia el modo de la apariencia
ventana.title("GARRAS, PERROS Y LLAVEROS S.A.")#asigna titulo a la ventana
ventana.geometry("800x500+300+100")#dimenciones de la ventana
def algoritmo_sugerencia():
    texto=entrada_texto.get()
    texto=texto.upper()
    cantidad_repeticionL={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0 }
    i= 0
    while i < len(texto):
        if texto[i] in cantidad_repeticionL:
            cantidad_repeticionL[texto[i]]+=1
        i+=1
    letra_masrepetida = max(cantidad_repeticionL, key=cantidad_repeticionL.get)
    r=("Te sugiero la letra "+str(letra_masrepetida)+" para tu recordatorio.")
    if cantidad_repeticionL[letra_masrepetida]==0:
        r="No hay letras"
    if cantidad_repeticionL[letra_masrepetida]==1:
        R=texto[0]
    resultado.configure(text=r)
    letra_elegida=letra_masrepetida
    letra_seleccionada=ctk.CTkLabel(ventana, text="Letra seleccionada: "+str(letra_elegida) , font=("consolas",20,"bold"))
    letra_seleccionada.pack()
    cambiarletra= ctk.CTkButton(ventana)
    cambiarletra.pack()
    imprimir= ctk.CTkButton(ventana)
    imprimir.pack()



#elementos de la ventana
Titulo=ctk.CTkLabel(ventana, text="GARRAS, PERROS Y LLAVEROS S.A.", font=("consolas",20,"bold"))
Titulo.pack()
cuadro1= ctk.CTkFrame(ventana)
cuadro1.pack()
Ingrese_texto=ctk.CTkLabel(cuadro1, text="Ingrese las palabras , frases o poemas de su preferencia: ", font=("consolas",20,"bold"))
Ingrese_texto.pack()
entrada_texto=ctk.CTkEntry(cuadro1,font=("consolas",20,"bold"),width=400 , height=100)
entrada_texto.pack()
cuadro2= ctk.CTkFrame(ventana)
cuadro2.pack()
resultado=ctk.CTkLabel(cuadro2, text="", font=("consolas",20,"bold"))
Enviar = ctk.CTkButton(ventana, text="Enviar", font=("arial",18),command=algoritmo_sugerencia)
Enviar.pack()
resultado.pack()


ventana.mainloop()