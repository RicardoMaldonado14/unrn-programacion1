sumador = 0
numingresados = 0
# Primera solicitud de datos
numero = int(input("Ingrese un numero: "))
# Bucle que procesa los números
while numero != 0: 
    sumador += numero
    numingresados += 1
    numero = int(input("Ingrese un numero: "))
# Impresión de resultados con validación para evitar división por cero
print(f"la suma total de los numeros es {sumador}")
print(f"la cantidad de numeros ingresados fue {numingresados}")

if numingresados > 0:
    promedio = sumador / numingresados
    print(f"el promedio de los numeros ingresados es {promedio}")
else:
    print("el promedio es 0 porque no se ingresaron números válidos")
