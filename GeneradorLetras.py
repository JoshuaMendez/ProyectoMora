ExteriorListaX = [100, 120, 120, 115, 115, 105, 105, 100, 100]
ExteriorListaY = [150, 150, 110, 110, 130, 130, 110, 110, 150]
InteriorListaX = []
InteriorListaY = []

#Especificaciones impresora
print(";Printing on: Dremel3D40 \n;Using material: ""PLA (0.75kg)"" \n;Quality: ""Medium Quality"" \n;FLAVOR:Marlin \n;TIME:691 \n;Filament used: 0.662266m \n;Layer height: 0.2 \n;MINX:-23.294 \n;MINY:-16.631 \n;MINZ:0.15 \n;MAXX:20.633 \n;MAXY:22.965 \n;MAXZ:2.95 \n;Generated with Cura_SteamEngine main \nM104 S220 \nM105 \nM109 S220 \nM82 ;absolute extrusion mode \nG28 \nG1 Z50.00 F400 \nG92 E0 \nG1 F200 E3 \nG92 E0 \nM132 X Y Z A \nM907 X100 Y100 Z50 A100 \nG92 E0 \nG92 E0 \nG1 F3600 E-3 \nM107 \nM106 S204")
print("")

#Contorno Exterior

ExteriorPosX = 0
ExteriorPosY = 0
DiferenciaExterior = 0
PosZ = 0.25
E = 0

print(";Contorno Exterior \n")

print("G0 X" + str(ExteriorListaX[0]), "Y" + str(ExteriorListaY[0]) + " Z0. \nG1 F3600 E0.03 \nG1 F600 Z" + str(PosZ))

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
        print("G1 F1500 X" + str(ExteriorListaX[1]), "Y" + str(ExteriorListaY[1]) + " E" + (str(E)))
    
    if ExteriorPosX > 1 and ExteriorPosY > 1 and ExteriorPosX < (len(ExteriorListaX) - 1) and ExteriorPosY < (len(ExteriorListaY) - 1):
        print("G1 X" + str(ExteriorListaX[ExteriorPosX]), "Y" + str(ExteriorListaY[ExteriorPosY]) + " E" + (str(E)))

    if DiferenciaExterior == (len(ExteriorListaX) - 1):

        E1 = abs(int(ExteriorListaX[-1]) - int(ExteriorListaX[0]))
        E2 = abs(int(ExteriorListaY[-1]) - int(ExteriorListaY[0]))

        if E1 != 0 and E2 == 0:
            RE = E1 * 0.03
        if E2 != 0 and E1 == 0:
            RE = E2 * 0.03

        E = E + RE 
        E = round(E, 3)

        print("G1 X" + str(ExteriorListaX[ExteriorPosX]), "Y" + str(ExteriorListaY[ExteriorPosY]) + " E" + (str(E)))


    ExteriorPosX = ExteriorPosX + 1
    ExteriorPosY = ExteriorPosY + 1

print("\n;Contorno Interior \n")

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
        print("G1 X" + str(InteriorListaX[1]), "Y" + str(InteriorListaY[1]) + " E" + (str(E)))
    
    if InteriorPosX > 0 and InteriorPosY > 0 and InteriorPosX < (len(InteriorListaX) - 1) and InteriorPosY < (len(InteriorListaY) - 1):
        print("G1 X" + str(InteriorListaX[InteriorPosX]), "Y" + str(InteriorListaY[InteriorPosY]) + " E" + (str(E)))

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

        print("G1 X" + str(InteriorListaX[-1]), "Y" + str(InteriorListaY[-1]) + " E" + (str(round(E))))

#Relleno vertical 1

x = 100
e = 3003.066
while x < 120.3:
    x = x + 0.3
    e = e + (0.03 * 29.4)
    print("G0 X" + str(round(x, 1)) + " Y149.7")
    print("G1 X" + str(round(x, 1)) + " Y120.3 E" + str(round(e, 3)))  

x = 120.3
e = 3063.042
while x < 146.7:
    x = x + 0.3
    e = e + (0.03 * 132.4)
    print("G0 X" + str(round(x, 1)) + " Y149.7")
    print("G1 X" + str(round(x, 1)) + " Y17.3 E" + str(round(e, 3)))

#Relleno vertical 3

x = 146.7
e = 3412.578
while x < 166.7:
    x = x + 0.3
    e = e + (0.03 * 29.4)
    print("G0 X" + str(round(x, 1)) + " Y149.7")
    print("G1 X" + str(round(x, 1)) + " Y120.3 E" + str(round(e, 3)))  

#Relleno horizontal 1

Y = 150
e = 3495.6
while Y > 120.3:
    Y = Y - 0.3
    e = e + (0.03 * 66.4)
    print("G0 X100.3" + " Y" + str(round(Y, 3)))
    print("G1 X166.7" + " Y" + str(round(Y, 3)) + " E" + str(round(e, 3)))

#Relleno horizontal 2

Y = 120.3
e = 3692.808
while Y > 17.3:
    Y = Y - 0.3
    e = e + (0.03 * 27)
    print("G0 X120.3" + " Y" + str(round(Y, 3)))
    print("G1 X146.7" + " Y" + str(round(Y, 3)) + " E" + str(round(e, 3)))