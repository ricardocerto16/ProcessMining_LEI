file = open("eventLog.csv","r")
file2 = open("log.csv","w")
#print("open file")

for line in file:
    prev = line.split(",")
    datainicio = prev[4] + "/" + prev[5] + "/" + prev[6] + " " + prev[7] + ":" + prev[8]
    datafinal = prev[9] + "/" + prev[10] + "/" + prev[11] + " " + prev[12] + ":" + prev[13]
    material = prev[1]
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
    line = prev[0] + "," + material + "," + seq + "," + prev[3] + "," + datainicio + "," + datafinal + "," + "\n"
    file2.writelines(line)


file.close()
#print("close file")