from datetime import datetime, timedelta

# pip install datetime_truncate
# truncate(datetime(2012, 2, 4, 12, 24, 50), 'minute')
now = datetime(2012, 2, 4, 12, 24)

#now = datetime.now()
print("Tupla de Datetime: " + str(now))

td = timedelta(minutes=24)
print("Time delta: " + str(td) + "\n")


print("Hora Atual " + str(now))

print("+24 horas " + str(now + td))
print("-24 horas " + str(now - td))
