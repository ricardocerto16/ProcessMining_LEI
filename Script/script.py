from datetime import datetime, timedelta

file = open("1_prod_cada.csv","r")
file2 = open("log1prod.csv","w")

for line in file:
    prev = line.split(",")
    datainicio = datetime(int(prev[18]),int(prev[19]), int(prev[20]), int(prev[21]), int(prev[22]))
    dataf = datetime(int(prev[23]),int(prev[24]),int(prev[25]),int(prev[26]),int(prev[27]))


    for x in range(1, 16):
        if prev[x] != '0':
          material = prev[x]
          break


    maquina = prev[17]
    if material == '1':
        material = "Vaso Simples"
        seq = "1 -> 2 -> 4"
    if material == '2':
        material = "Azulejo Decorativo"
        seq = "1 -> 3 -> 4 -> 5 -> 6"
    if material == '3':
        material = "Jarra"
        seq = "1 -> 2 -> 4 -> 6"
    if material == '4':
        material = "Floreira Pintada"
        seq = "1 -> 2 -> 4 -> 5"
    if material == '5':
        material = "Tijolo"
        seq = "2 -> 4"
    if material == '6':
        material = "Taca Ondulada"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
        td = timedelta(minutes=10)
        dataf = str(dataf + td)
    if material == '7':
        material = "Prato Simples"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
    if material == '8':
        material = "Prato Pintado"
        seq = "1 -> 2 -> 4 -> 5 -> 6"
    if material == '9':
        material = "Tijolo Cortado"
        seq = "2 -> 3 -> 4"
    if material == '10':
        material = "Cinzeiro"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
        td = timedelta(minutes=3)
        dataf = str(dataf + td)
    if material == '11':
        material = "Copo Festivo"
        seq = "1 -> 2 -> 3 -> 4 -> 5"
    if material == '12':
        material = "Jarra Pintada"
        seq = "1 -> 2 -> 4 -> 5 -> 6"
    if material == '13':
        material = "Cao de Barro"
        seq = "1 -> 2 -> 3 -> 4 -> 5 -> 6"
        td = timedelta(minutes=25)
        dataf = str(dataf + td)
    if material == '14':
        material = "Garrafeira de Barro"
        seq = "1 -> 2 -> 3 -> 4"
    if material == '15':
        material = "Pipo de Barro Pintado"
        seq = "1 -> 2 -> 3 -> 4 -> 5 -> 6"
        td = timedelta(minutes=10)
        dataf = str(dataf + td)
    if material == '16':
        material = "Assadar de Chouriço em Barro"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
        td = timedelta(minutes=15)
        dataf = str(dataf + td)


    if (maquina == "Maquina1.1" or maquina == "Maquina1.2" or maquina == "Maquina1.3"):
        maquina = maquina + " -> Preparacao"
    if (maquina == "Maquina2.1" or maquina == "Maquina2.2" or maquina == "Maquina2.3"):
        maquina = maquina + " -> Moldagem"
    if (maquina == "Maquina3.1" or maquina == "Maquina3.2" or maquina == "Maquina3.3"):
        maquina = maquina + " -> Corte"
    if (maquina == "Maquina4.1" or maquina == "Maquina4.2" or maquina == "Maquina4.3"):
        maquina = maquina + " -> Cozedura"
    if (maquina == "Maquina5.1" or maquina == "Maquina5.2" or maquina == "Maquina5.3"):
        maquina = maquina + " -> Pintura"
    if (maquina == "Maquina6.1" or maquina == "Maquina6.2" or maquina == "Maquina6.3"):
        maquina = maquina + " -> Envernizamento"


    #datafinal = dataf

    line = prev[0] + "," + material + "," + seq + "," + maquina + "," + str(datainicio) + "," + str(dataf) + "," + "\n"
    file2.writelines(line)


file.close()
#print("close file")