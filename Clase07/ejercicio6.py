numero = int(input("ingrese un numero (pulse 0 para terminar): "))
numeros = []
num_positivos = 0
num_negativos = 0 
sumatotal = 0
while numero != 0:
    numeros.append(numero)
    if numero > 0:
        num_positivos +=1
    if numero < 0:
        num_negativos+=1
    sumatotal += numero
    numero = int(input("ingrese un numero (pulse 0 para terminar): "))

print(f"cantidad de numeros positivos: {num_positivos}")
print(f"cantidad de numeros negativos: {num_negativos}")
print(f"la suma total es: {sumatotal}")