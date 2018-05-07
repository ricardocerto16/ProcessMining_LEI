file = open("500chance.csv","r")
file2 = open("log500chance.csv","w")
#print("open file")

for line in file:
    prev = line.split(",")
    datainicio = prev[4] + "/" + prev[5] + "/" + prev[6] + " " + prev[7] + ":" + prev[8]
    datafinal = prev[9] + "/" + prev[10] + "/" + prev[11] + " " + prev[12] + ":" + prev[13]
    material = prev[1]
    maquina = prev[3]
    if material == '4':
        material = "Vaso Simples"
        seq = "1 -> 2 -> 4"
    if material == '5':
        material = "Azulejo Decorativo"
        seq = "1 -> 3 -> 4 -> 5 -> 6"
    if material == '6':
        material = "Jarra"
        seq = "1 -> 2 -> 4 -> 6"
    if material == '7':
        material = "Floreira Pintada"
        seq = "1 -> 2 -> 4 -> 5"
    if material == '8':
        material = "Tijolo"
        seq = "2 -> 4"
    if material == '9':
        material = "Taça Ondulada"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
    if material == '10':
        material = "Prato Simples"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
    if material == '11':
        material = "Prato Pintado"
        seq = "1 -> 2 -> 4 -> 5 -> 6"


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




    line = prev[0] + "," + material + "," + seq + "," + maquina + "," + datainicio + "," + datafinal + "," + "\n"
    file2.writelines(line)


file.close()
#print("close file")