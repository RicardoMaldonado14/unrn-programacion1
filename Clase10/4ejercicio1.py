archivo = open("4nombres.txt", "r")
listanombres= archivo.readlines()
archivo.close()

idx=0
for nombre in listanombres:
    print(idx, nombre.strip())
    idx +=1