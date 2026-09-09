

from datetime import datetime, timedelta

fecha = datetime(2026, 9, 2, 17, 30)
vencimiento = fecha + timedelta(days=7)

print(vencimiento)


#diferencia de fechas
from datetime import datetime

fecha_1 = datetime(2026, 9, 1, 8, 15)
fecha_2 = datetime(2026, 9, 4, 10, 30)

diferencia = fecha_2 - fecha_1

print(diferencia)
print(diferencia.days)