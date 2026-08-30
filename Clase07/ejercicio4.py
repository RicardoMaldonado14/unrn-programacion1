def sumapares(argumento):
    sumatotal = 0
    for i in argumento:
        if i%2 == 0:
            sumatotal += i
    return sumatotal


numeros = [2, 4, 5, 7, 9, 10, 12]

print(f"la suma de los numeros pares de la lista es: {sumapares(numeros)}")