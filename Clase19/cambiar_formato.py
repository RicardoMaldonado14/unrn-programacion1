from datetime import datetime

entrada = "2026-09-15T18:25:30"
fecha = datetime.strptime(entrada, "%Y-%m-%dT%H:%M:%S")
print(fecha)
fechanueva = fecha.strftime("%d/%m/%Y %H:%M")