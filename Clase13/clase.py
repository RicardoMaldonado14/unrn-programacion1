# con el for clasico
cuadrados1 = []
for x in range(5):
    cuadrados1.append(x**2)
print(cuadrados1)


#con comprension:
cuadrados = [x**2 for x in range (5)]
print(cuadrados)

trios = [(x, y, z) for x in [1, 2, 3] for y in ["a", "b"] for z in[3, 2, 1]]
print(trios)



#con comprension
productos = {"teclado": 120, "mouse": 80, "monitor": 450}
nuevos_precios = {prod: (precio * 0.9 if precio > 100 else precio) for prod,
precio in productos.items()}
print (nuevos_precios)