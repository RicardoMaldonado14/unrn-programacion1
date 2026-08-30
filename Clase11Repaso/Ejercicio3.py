# Armar una nueva lista llamada nombres_normalizados donde 
# cada nombre quede sin espacios sobrantes y con un formato prolijo.
# Al final, mostrar la lista. Deberia quedar parecido a esto:

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []

for nombre in nombres:
    nombre_limpio = nombre.strip().capitalize()
    nombres_normalizados.append(nombre_limpio)

print(nombres_normalizados)