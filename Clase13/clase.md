la comprension de listas es una forma compacta de construir una lista a partir
de un iterable

cuadrados = []
for x in range(5):
    cuadrados.append(x**2)

#con comprension:

cuadrados = [x**2 for x in range (5)]

diccionarios por comprension
la comprension de diccionarios es una forma compacta de constrir 
un diccionario a partir de un iterable


comprensiones anidadas
se pueden tener varios ciclos for dentro de una misma comprension
#con for clasico
pares = []
    for x in [1, 2, 3]:
        for y in ["a", "b"]:
         pares.append((x,y))

#con comprension:
pares = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]

trios = [(x, y, z) for x in [1, 2, 3] for y in ["a", "b"] for z in[3, 2, 1]]

obetener lista de cuadrados pares con for clasico:
cuadrados1 = []
for x in range(5):
    if (x**2)%2==0:
        cuadrados1.append(x**2)
print(cuadrados1)

obetener lista de cuadrados pares con comprension
cuadrados = [x**2 for x in range (5) if (x**2) % 2 == 0]


#con comprension
notas = [4, 7, 5, 9, 6]
estados = ["aprobado" if n >= 6 else "desaprobado" for n in notas]

productos = {"teclado": 120, "mouse": 80, "monitor": 450}

#con comprension
nuevos_precios = {prod: (precio * 0.9 if precio > 100 else precio) for prod,
precio in productos.items()}