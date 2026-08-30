listanombres = []
while len(listanombres)<5:
    nombre = input("ingrese un nombre: ")
    listanombres.append(nombre)

archivo = open("texto.txt", "w")

archivo.writelines("\n".join(listanombres))

archivo.close()

