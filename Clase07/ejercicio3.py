numeros = [-1, 1, -2, -3, 7, 10]
num_positivos = 0
num_negativos = 0 
sumatotal = 0
for num in numeros:
    if num > 0:
        num_positivos +=1
    if num < 0:
        num_negativos+=1
    sumatotal += num

print(f"cantidad de numeros positivos: {num_positivos}")
print(f"cantidad de numeros negativos: {num_negativos}")
print(f"la suma total es: {sumatotal}")