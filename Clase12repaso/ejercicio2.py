# [3.2, 3.4, 5.1, 2.9, 6.0, 3.3]
# Mostrar cuántas mediciones están fuera del rango
# 3.0 a 5.0
mediciones = [3.2, 3.4, 5.1, 2.9, 6.0, 3.3]
medicionesrango = []
for medicion in mediciones:
    if 3.0 > medicion or medicion > 5.0:
        medicionesrango.append(medicion)
print(f"las mediciones {medicionesrango} estan fuera de rango ")