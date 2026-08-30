import sys

rutaarchivo = sys.argv[1]
posicion = sys.argv[2]
palabras = None

with open(rutaarchivo, "r") as archivo:
    palabras = archivo.readline().split(" ")
    print(palabras)