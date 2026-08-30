def sumapares(argumento):
    sumatotal = 0
    for i in argumento:
        if i%2 == 0:
            sumatotal += i
    return sumatotal

numeros = []
estado = True
print("---ingrese 5 numeros---")
while estado:
    numero = int(input("ingrese un numero: "))
    numeros.append(numero)
    if len(numeros) == 5:
        estado = False
    
print(f"la suma de sus numeros pares es: {sumapares(numeros)}")
