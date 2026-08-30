#Tenés una lista de tuplas con datos semanales de temperatura máxima por ciudad y fecha:
# Resolver:
# Mostrar todas las ciudades sin repetir (usar set).
# Mostrar todas las fechas disponibles sin repetir.
# Calcular el promedio de temperatura por ciudad (usar diccionario).
# Indicar qué ciudad tuvo el mayor promedio.
registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]
ciudades = []
fechas = []
for registro in registros:
    ciudades.append(registro[1])
    fechas.append(registro[0])
ciudadesunicas=set(ciudades)
fechasunicas=set(fechas)
print(ciudadesunicas)

# Calcular el promedio de temperatura por ciudad (usar diccionario).
temperaturasxciudad = {}
for registro in registros:
    fecha, ciudad, temp = registro
    if ciudad not in temperaturasxciudad:
        temperaturasxciudad[ciudad] = []
    temperaturasxciudad[ciudad].append(temp)
print(temperaturasxciudad)

promedios = {}
for ciudad, listatemps in temperaturasxciudad.items():
    promedios[ciudad] = sum(listatemps)/len(listatemps)

print(promedios)
prom_max = 0
ciudad_max = None
for ciudad, promedio in promedios.items():
    if promedio > prom_max: 
        prom_max = promedio
        ciudad_max = ciudad

print(f"{ciudad_max} tuvo {prom_max}")