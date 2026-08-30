listanombres = []

for num in range(5):
    nombre = input(f"ingresar el nombre N {num} ")
    listanombres.append(nombre)

archivo = open("6ej3_archivo.txt", "w")
archivo.write("\n".join(listanombres))
archivo.close()