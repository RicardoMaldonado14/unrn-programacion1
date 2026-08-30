numero = int(input("ingrese un numero: "))
numeros = []
while numero != 0:
    numeros.append(numero)
    numero = int(input("ingrese un numero: "))

if len(numeros)>0:
    maximo = numeros[0]
    minimo = numeros[0]

    for i in numeros:
        if i>maximo:
            maximo=i
        elif i<minimo:
            minimo=i

    print(f"el numero mas grande es {maximo}")
    print(f"el numero mas chico es {minimo}")

if len(numeros)==0:
    print("no hay numeros para comparar")