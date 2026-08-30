# Mostrar el primer y el último valor.
# Contar cuántas veces aparece el número 7.
# Mostrar el largo de la tupla.
numeros = (4, 7, 2, 9, 7)
print(f"el primer valor es {numeros[0]}, el ultimo valor es {numeros[-1]}")
print(len(numeros))

contador = 0
for i in numeros:
    if i == 7:
        contador +=1

print(f"el numero 7 aparece {contador} veces")