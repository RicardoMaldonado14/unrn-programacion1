x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]
maximo = x[0]
minimo = x[0]
for i in x:
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i
print(maximo)
print(minimo)