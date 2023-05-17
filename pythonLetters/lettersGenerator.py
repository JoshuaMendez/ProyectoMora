from lettersFunctionalities import *

llamarLetras()

ExteriorListaX = [100, 120, 120, 115, 115, 105, 105, 100, 100] # Lista que almacena las coordenadas X del contorno externo de las letras
ExteriorListaY = [150, 150, 110, 110, 130, 130, 110, 110, 150] # Lista que almacena las coordenadas Y del contorno externo de las letras
InteriorListaX = [] # Lista que almacena las coordenas interiores X, todos estos valores se calculan en el código de abajo
InteriorListaY = [] # Lista que almacena las coordendas interiores Y, todos estos valores se calculan en el código de abajo
rellenoHorizontalLista =[] # Lista que almacena cómo iría el relleno horizontal de las letras
rellenoVerticalLista = [] # Lista que almacena cómo iría el relleno vertical de las letras


#Especificaciones impresora
# Empezamos en 0s (Centro)

ExteriorPosX = 0
ExteriorPosY = 0
DiferenciaExterior = 0
PosZ = 0.25
E = 0

# Halla la diferencia que hay entre una coordenada y la que sigue para conseguir el valor por el cual se va a multiplicar.
# También imprime las coordenadas.

while ExteriorPosX < len(ExteriorListaX) and ExteriorPosY < len(ExteriorListaY): 

    # Calcula la diferencia para que no se salga de la lista
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
    # Si este valor es igual a 0 imprime un G0
    if ExteriorPosX == 0 and ExteriorPosY == 0:
        ExteriorListaX
    # Si este valor es mayor a 1 y menor a los otros valores, las imprime como G1
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

# Para el contorno interior se utilizan las coordenadas ya ingresadas y se le resta o suma 0.3

InteriorPosX = 0
InteriorPosY = 0
DiferenciaInterior = 0
# dependiendo de donde esté ubicada, si el valor menos 0.3 es menor a 100 entonces le suma 0.3
while InteriorPosX < len(ExteriorListaX) and InteriorPosY < len(ExteriorListaY):

    if ExteriorListaX[InteriorPosX] - 0.3 < 100:
        ValorInterior = ExteriorListaX[InteriorPosX] + 0.3
        InteriorListaX.append(ValorInterior)
    
    else:
        # y si la coordenada más 0.3 es mayor 120 entonces le resta 0.3 y se toma un punto medio de
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
        # referencia el cual es 110 para que lo evalúe en 3 casos diferentes y se realiza el mismo
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
# procedimiento con las coordenadas de Y. Este resultado se almacena en las listas Interioristas e
# Interiorista y se hace el mismo proceso para hallar los valores de E.
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

# Ya con los contornos se hace el relleno vertical y horizontal en donde se ingresa la coordenada
# inicial de X y este va sumando 0.3 hasta llegar a 120 que es la coordenada final y se establecen
# los valores de Y, tanto el punto inicial como el punto final y se imprime un G0 y un G1 intercalados
# para que siempre vuelve a la parte superior de la letra. Se ingresa el último valor que tomó E y la
# distancia que va a recorrer y cada que avance 0.3 en X esta distancia se va a multiplicar por
# 0.03 para conseguir el valor final de Y.

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

# Se realiza el mismo procedimiento para el relleno horizontal solo que las coordenadas que
# varían van a ser las de Y. Se realiza todo este proceso hasta que el valor en Z sea 2 lo cual
# equivale a las 8 capas que contiene la letra y se obtiene el código G que se envía a la impresora.