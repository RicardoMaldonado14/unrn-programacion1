import json

with open("guardia_house.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)

print(datos["guardia"])

for paciente in datos["pacientes"]:
    print(paciente)

    if paciente["prioridad"] == "alta":
        print(f"el paciente {paciente["nombre"]} es de alta prioridad")