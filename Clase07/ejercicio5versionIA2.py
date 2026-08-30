def sumapares_alternativa(argumento):
    # Filtra los pares y usa sum() para sumarlos todos juntos
    pares = [i for i in argumento if i % 2 == 0]
    return sum(pares)

numeros = []
print("--- Ingrese 5 números ---")

# Se ejecuta exactamente 5 veces
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

resultado = sumapares_alternativa(numeros)
print(f"La suma de sus números pares es: {resultado}")
