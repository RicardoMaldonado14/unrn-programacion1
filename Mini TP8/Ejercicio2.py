# Escribí un programa que:
# Cree un diccionario donde la clave sea la ubicación.
# Cada ubicación debe guardar una lista con sus mediciones.
# Cree un conjunto con todos los tipos de medición sin repetir.
# Muestre el diccionario final.
# Muestre el conjunto de tipos encontrados.
mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

diccionario = {}
mediciontipo = set()
for tupla in mediciones:
    tipo = tupla[0]
    valor = tupla[1]
    ubicacion = tupla[2]

    mediciontipo.add(tipo)
    if ubicacion not in diccionario:
        diccionario[ubicacion]=[]
    diccionario[ubicacion].append((tipo, valor))

print("el diccionario final es: ")
print(diccionario)

print(f"los tipos de medicion encontrados son: {mediciontipo}")