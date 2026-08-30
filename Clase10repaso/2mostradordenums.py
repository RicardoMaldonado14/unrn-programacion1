numeros = []

archivo = open("numeros.txt", "r")
for numero in archivo.readlines():
    numeros.append(int(numero))

archivo.close()

print(numeros)
print(f"la suma de los numeros es {sum(numeros)}")