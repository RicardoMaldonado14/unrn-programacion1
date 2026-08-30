def sumapares(argumento):
    sumatotal = 0
    for i in argumento:
        if i % 2 == 0:
            sumatotal += i
    return sumatotal

numeros = []
print("--- Ingrese 5 números ---")

# El bucle se detiene directamente cuando la lista tiene 5 elementos
while len(numeros) < 5:
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    
print(f"La suma de sus números pares es: {sumapares(numeros)}")
