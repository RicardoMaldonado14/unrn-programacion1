listanombres = []

archivo = open("nombres.txt", "r")

for nombre in archivo.readlines():
    listanombres.append(nombre.strip())
archivo.close()

for nombre in range(len(listanombres)):
    print(nombre, listanombres[nombre])