numero = int(input("Ingrese un numero: "))
sumador = 0
numingresados = 0
while numero != 0: 
    sumador +=numero
    numingresados +=1
    numero = int(input("Ingrese un numero: "))
promedio = sumador/numingresados


print(f"la suma total de los numeros es {sumador}")
print(f"la cantidad de numeros ingresados fue {numingresados}")
print(f"el promedio de los numeros ingresados es {promedio}")