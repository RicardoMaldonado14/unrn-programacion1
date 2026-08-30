archivo = open("nombredoc.csv", "w")

for i in range(5):
    nombre = input("ingrese un nombre: ")
    documento = input("ingrese el documento: ")

    archivo.write(f"el nombre es {nombre} y su documento {documento}\n")

archivo.close()