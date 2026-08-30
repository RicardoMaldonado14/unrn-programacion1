palabras = []
archivo = open("frases.txt", "r")

for frase in archivo.readlines():
    palabras += frase.split(" ")

archivo.close()
posicion = input("ingrese la posicion deseada: ")

print