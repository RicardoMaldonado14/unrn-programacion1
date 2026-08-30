# Partiendo de esta lista:
# nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
# Armar una nueva lista llamada nombres_normalizados donde cada nombre quede sin espacios sobrantes y con un formato prolijo.
# Al final, mostrar la lista. Deberia quedar parecido a esto:
# ["Mara", "Tomas", "Lucia", "Marcos", "Sofia"]

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombresnormalizados = []
for nombre in nombres:
    nombrenormal = nombre.strip().capitalize()
    nombresnormalizados.append(nombrenormal)

print(nombresnormalizados)