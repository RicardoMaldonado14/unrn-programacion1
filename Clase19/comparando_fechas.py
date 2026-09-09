from datetime import datetime

fecha_1 = datetime.strptime("01/09/2026 08:15", "%d/%m/%Y %H:%M")
fecha_2 = datetime.strptime("01/09/2026 10:30", "%d/%m/%Y %H:%M")

if fecha_1 < fecha_2:
    print("La primera fecha ocurre antes")
elif fecha_1 > fecha_2:
    print("La segunda fecha ocurre antes")
else:
    print("Las fechas son iguales")