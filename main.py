from PIL import ImageTk, Image
import tkinter as tk
import customtkinter as ctk
ventana = ctk.CTk() # configuracion de la ventana
ventana._set_appearance_mode("dark")  # cambia el modo de la apariencia 
ventana.title("Garras, Perros y Llaveros S.A. - Recuerdos") # asigna titulo a la ventana
ventana.geometry("1270x720")  # dimensiones de la ventana
letra_elegida = ""

def funcion_imprimir():
    global letra_elegida
    boton_confrimar=ctk.CTkButton(ventana, text="Confirmar", font=("arial", 18), height=50, width=200)
    boton_confrimar.place(x=100,y=550)
    if letra_elegida=="A":
        img= ctk.CTkImage(dark_image=Image.open("Desktop\ProyectoMora\letraA.jpg"), size=(300, 300))
    
    grafico=ctk.CTkLabel(ventana,text="",image=img, height=300, width=300)
    grafico.place(x=100,y=200)
  
def funcion_aceptar():
    global nuevaLetra, letra_elegida
    nuevaLetra = entrada_letranueva.get()
    mensaje_error= ctk.CTkLabel(ventana,text="",font=("consolas", 18, "bold"))
    mensaje_error.place(x=500,y=550)
    mensaje_error.configure(text="")
    if nuevaLetra.isdigit():
        mensaje_error.configure(text="¡Eso no parece una letra!")
        return False
    if len(nuevaLetra) > 1 or len(nuevaLetra) == 0:
        mensaje_error.configure(text="¡Recuerda que las letras tienen 1 caracter!")
        print('es más de un caracter')
        return False
    else:
        print('correcto')
        letra_elegida = nuevaLetra.upper()
        mensaje_error.configure(text="Se cambio exitosamente  ")
        letra_seleccionada.configure(text="Letra seleccionada: "+str(letra_elegida))

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


def algoritmo_sugerencia():
    global letra_elegida, letra_seleccionada, cambiarletraboton, imprimir, cantidad_repeticionL
    texto = entrada_texto.get()
    texto = texto.upper()
    cantidad_repeticionL = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
                            "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    i = 0
    while i < len(texto):
        if texto[i] in cantidad_repeticionL:
            cantidad_repeticionL[texto[i]] += 1
        i += 1
    letra_masrepetida = max(cantidad_repeticionL, key=cantidad_repeticionL.get)
    r = ("Te sugiero la letra "+str(letra_masrepetida)+" para tu recordatorio.")
    if cantidad_repeticionL[letra_masrepetida] == 0:
        r = "No hay letras"
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

def rankingMasRepetida():
    print('hola')

# elementos de la ventana principal
Titulo = ctk.CTkLabel(
    ventana, text="Garras, Perros y Llaveros S.A.", font=("consolas", 25, "bold"))
Titulo.place(x=340, y=30)
Ingrese_texto = ctk.CTkLabel(ventana, text="Ingrese las palabras , frases o poemas de su preferencia: ", font=(
    "consolas", 18, "bold"), width=400, height=10)
Ingrese_texto.place(x=500, y=100)
entrada_texto = ctk.CTkEntry(ventana, font=(
    "consolas", 12, "bold"), width=550, height=50)
entrada_texto.place(x=500, y=150)
resultado = ctk.CTkLabel(ventana, text="", font=("consolas", 14, "bold"))
Enviar = ctk.CTkButton(ventana, text="Enviar", font=(
    "arial", 18), command=algoritmo_sugerencia, height=50, width=200)
Enviar.place(x=500, y=230)
resultado.place(x=710, y=230)


ventana.mainloop()
