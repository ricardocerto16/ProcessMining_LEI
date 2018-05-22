# coding=utf-8
import random
from datetime import datetime, timedelta
import numpy

file = open("500_prod_cada.csv", "r")
file2 = open("log500prod.csv", "w")

for line in file:
    prev = line.split(",")
    datainicio = datetime(int(prev[18]), int(prev[19]), int(prev[20]), int(prev[21]), int(prev[22]))
    dataf = datetime(int(prev[23]), int(prev[24]), int(prev[25]), int(prev[26]), int(prev[27]))

    for x in range(1, 17):
        if prev[x] != '0':
            material = prev[x]
            break

    td = timedelta(minutes=0)
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

    if material == '11':
        material = "Copo Festivo"
        seq = "1 -> 2 -> 3 -> 4 -> 5"

    if material == '12':
        material = "Jarra Pintada"
        seq = "1 -> 2 -> 4 -> 5 -> 6"

    if material == '13':
        material = "Cao de Loica"
        seq = "1 -> 2 -> 3 -> 4 -> 5 -> 6"
        td = timedelta(minutes=25)

    if material == '14':
        material = "Garrafeira de Barro"
        seq = "1 -> 2 -> 3 -> 4"

    if material == '15':
        material = "Pipo de Barro Pintado"
        seq = "1 -> 2 -> 3 -> 4 -> 5 -> 6"
        td = timedelta(minutes=10)

    if material == '16':
        material = "Assador de Chourico em Barro"
        seq = "1 -> 2 -> 3 -> 4 -> 6"
        td = timedelta(minutes=15)




    maquina = prev[17]

    if maquina == "Maquina1.1":
        maquina = maquina + " -> Preparacao"
        tempo = timedelta(minutes=random.choice([3, 4, 5, 6, 7, 8]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina1.2":
        maquina = maquina + " -> Preparacao"
        tempo = timedelta(minutes=random.choice([3, 4, 5, 6, 7, 8]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.2, 0.15, 0.3, 0.25, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina1.3":
        maquina = maquina + " -> Preparacao"
        tempo = timedelta(minutes=random.choice([3, 4, 5, 6, 7, 8]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.05, 0.3, 0.05, 0.05, 0.5, 0.05]))
        dataf = str(datainicio + tempo + td + dp)




    if maquina == "Maquina2.1":
        maquina = maquina + " -> Moldagem"
        tempo = timedelta(minutes=random.choice([4, 7, 11]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5], p=[0.1, 0.2, 0.1, 0.1, 0.5]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina2.2":
        maquina = maquina + " -> Moldagem"
        tempo = timedelta(minutes=random.choice([4, 7, 12]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 6], p=[0.1, 0.2, 0.5, 0.05, 0.05, 0.1]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina2.3":
        maquina = maquina + " -> Moldagem"
        tempo = timedelta(minutes=random.choice([4, 8, 10]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 6], p=[0.05, 0.1, 0.2, 0.1, 0.5, 0.05]))
        dataf = str(datainicio + tempo + td + dp)




    if maquina == "Maquina3.1":
        maquina = maquina + " -> Corte"
        tempo = timedelta(minutes=random.choice([4, 5, 6, 7, 8, 9]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.7, 0.1, 0.05, 0.05, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina3.2":
        maquina = maquina + " -> Corte"
        tempo = timedelta(minutes=random.choice([4, 5, 6, 7, 8]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 4, 6], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina3.3":
        maquina = maquina + " -> Corte"
        tempo = timedelta(minutes=random.choice([4, 5, 6, 7, 8, 9]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.3, 0.4, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)



    if maquina == "Maquina4.1":
        maquina = maquina + " -> Cozedura"
        tempo = timedelta(minutes=random.choice([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        dp = timedelta(minutes=numpy.random.choice([0, 5, 8, 7, 10, 12], p=[0, 0, 0.35, 0.4, 0.2, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina4.2":
        maquina = maquina + " -> Cozedura"
        tempo = timedelta(minutes=random.choice([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        dp = timedelta(minutes=numpy.random.choice([0, 5, 8, 7, 10, 12], p=[0.2, 0.1, 0.1, 0.1, 0.4, 0.1]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina4.3":
        maquina = maquina + " -> Cozedura"
        tempo = timedelta(minutes=random.choice([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        dp = timedelta(minutes=numpy.random.choice([0, 5, 7, 8, 10, 12], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina4.4":
        maquina = maquina + " -> Cozedura"
        tempo = timedelta(minutes=random.choice([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        dp = timedelta(minutes=numpy.random.choice([0, 5, 7, 8, 10, 12], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)



    if maquina == "Maquina5.1":
        maquina = maquina + " -> Pintura"
        tempo = timedelta(minutes=random.choice([3, 4, 5, 6, 7, 8, 9, 10]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina5.2":
        maquina = maquina + " -> Pintura"
        tempo = timedelta(minutes=random.choice([3, 4, 5, 6, 7, 8, 9, 10]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.1, 0.2, 0.1, 0.5, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina5.3":
        maquina = maquina + " -> Pintura"
        tempo = timedelta(minutes=random.choice([3, 4, 5, 6, 7, 8, 9, 10]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 5, 7], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)




    if maquina == "Maquina6.1":
        maquina = maquina + " -> Envernizamento"
        tempo = timedelta(minutes=random.choice([2, 3, 4, 5]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 4, 5], p=[0.2, 0.1, 0.1, 0.5, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina6.2":
        maquina = maquina + " -> Envernizamento"
        tempo = timedelta(minutes=random.choice([2, 3, 4, 5]))
        dp = timedelta(minutes=numpy.random.choice([0, 1, 2, 3, 4, 5], p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)

    if maquina == "Maquina6.3":
        maquina = maquina + " -> Envernizamento"
        tempo = timedelta(minutes=random.choice([2, 3, 4, 5]))
        dp = timedelta(minutes=numpy.random.choice([0, 0, 0, 3, 4, 5], p=[0.75, 0.05, 0.05, 0.05, 0.05, 0.05]))
        dataf = str(datainicio + tempo + td + dp)




    line = prev[0] + "," + material + "," + seq + "," + maquina + "," + str(datainicio) + "," + str(dataf) + "," + "\n"
    file2.writelines(line)

file.close()
