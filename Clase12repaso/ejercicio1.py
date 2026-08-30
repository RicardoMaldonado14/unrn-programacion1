# Un sensor registra eventos con este formato:
# "PUERTA_A;ABIERTA;18:03"
# "PUERTA_B;CERRADA;18:04"
# "PUERTA_A;ABIERTA;18:05"
# Se quiere contar cuántas veces aparece cada
# puerta.
registros = ("PUERTA_A;ABIERTA;18:03",
            "PUERTA_B;CERRADA;18:04",
            "PUERTA_A;ABIERTA;18:05")
conteo = {}
for registro in registros:
    partes = registro.split(";")
    puerta = partes[0].strip()
    if puerta in conteo:
        conteo[puerta] +=1
    else:
        conteo[puerta] = 1

for puerta, cantidad in conteo.items():
    print (f"la puerta {puerta} aparece {cantidad} veces")