# Leyendo linea a linea #
archivo = open("datos.txt", "r")
# Lee el archivo hasta encontrar una linea completa delimitada por \n
linea = archivo.readline()
print(linea.strip())    