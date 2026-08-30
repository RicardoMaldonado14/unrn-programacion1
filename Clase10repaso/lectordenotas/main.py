archivo = open("lectordenotas/datos/alumnos/notas.txt", "r")
for linea in archivo:
        print(linea.strip("\n"))

archivo.close()
