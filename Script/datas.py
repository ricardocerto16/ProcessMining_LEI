from datetime import datetime, timedelta

now = datetime.now()

print("Tupla de Datetime: " + str(now))

td = timedelta(minutes=24)
print("Time delta: " + str(td) + "\n")

print("Hora Atual " + str(now))
print("+24 horas " + str(now + td))
print("-24 horas " + str(now - td))
