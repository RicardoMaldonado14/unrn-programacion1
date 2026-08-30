#listas por comprension
# Con for clásico:
cuadrados = []
for x in range(5):
 cuadrados.append(x ** 2)
# Con comprensión:
cuadrados = [x ** 2 for x in range(5)]
print (cuadrados)


#diccionarios por comprension
# Con for clasico
cuadrados = {}
for x in range(5):
 cuadrados[x] = x ** 2
print(cuadrados)
# Con comprensión:
{x: x ** 2 for x in range(5)}


#varios ciclos for 
pares = []
for x in [1, 2, 3]:
    for y in ['a', 'b']:
        pares.append((x, y))
print(pares)

#trios
trios = [(x, y, z) for x in [1, 2, 3] for y in ['a', 'b'] for z in [3, 2, 1]]
print(trios)