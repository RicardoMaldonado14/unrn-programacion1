def funcion(lista):
    contador = 0
    maximo = int(lista[0])
    nummayor = []
        
    for i in lista:
        if i > maximo:
            maximo = i
    nummayor.append(maximo)
    for num in lista:
        if maximo in lista:
            contador += 1
    nummayor.append(contador)
        



numeros = [4, 9, 1, 9, 3]
print(funcion(numeros))