#la mayoria de los lenguajes trae herramientas p/ trabajar con fechas
# en python usamos datetime

#cuando una fecha pasa de str a datetime, python puede ayudarnos a
#validar si existe 


#idea central:
# texto -> datetime -> texto
#



#importar datetime
#
from datetime import datetime

import time


print(datetime.now())

time.sleep(1)

print(datetime.now())

#partes de una fecha

ahora = datetime.now()

print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)
print(ahora.microsecond)



#extrayendo fecha de un string: strptime

texto= "02/09/2026"

print(datetime.strptime("02/09/2026 17:30", "%d/%m/%Y %H:%M"))