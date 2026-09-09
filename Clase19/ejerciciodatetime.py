from datetime import datetime

fechas = {
    "21-08-2026 18:45:20",
    "2026/08/21 07:30",
    "21.08.26"
}
fechaslimpias = []
validez = True
for fecha in fechas:
    fecha_limpia = datetime.strptime(fecha, "%d-%m-%Y %H:%M:%S") or fecha_limpia = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
