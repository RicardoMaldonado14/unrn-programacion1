# Escribí un programa que:
# Lea el archivo línea por línea.
# Separe cada línea usando split(";").
# Genere un diccionario donde:
# la clave sea la ciudad;
# el valor sea una lista de temperaturas registradas.
# Muestre el diccionario final.

archivo = open("temperaturas.txt", "r")


diccionario = {}
for linea in archivo:
    ciudad, valor = linea.strip().split(";")

    valor = int(valor)

    if ciudad not in diccionario:
        diccionario[ciudad]=[]
    diccionario[ciudad].append(valor)
archivo.close()

print(diccionario)
