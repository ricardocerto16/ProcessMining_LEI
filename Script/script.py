file = open("eventLog.csv","r")
file2 = open("log.csv","w")
#print("open file")

for line in file:
    prev = line.split(",")
    datainicio = prev[3] + "/" + prev[4] + "/" + prev[5] + " " + prev[6] + ":" + prev[7]
    datafinal = prev[8] + "/" + prev[9] + "/" + prev[10] + " " + prev[11] + ":" + prev[12]
    line = prev[0] + "," + prev[1] + "," + prev[2] + "," + datainicio + "," + datafinal + "," + "\n"
    file2.writelines(line)


file.close()
#print("close file")