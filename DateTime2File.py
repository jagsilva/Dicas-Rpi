import datetime

hora = datetime.datetime.now()

file = open("log.txt", "a")
file.write("\n"+str(hora))
file.close()
