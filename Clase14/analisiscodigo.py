registros_temperatura = [
    "FREY;12",
    "OTTO;8°C",
    "CATEDRAL;8",
    "FREY;5"
]

total = 0

for registro in registros_temperatura:
    if registro.count(";") != 1:
        print("Error en el registro ", registro, "se descarta")
        continue

    nombre, temperatura = registro.split(";")
    if temperatura.isnumeric():
            total += int(temperatura)


print(total)