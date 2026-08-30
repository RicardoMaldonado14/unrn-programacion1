nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
num=0
nombres_normalizados=[]
for i in nombres:
    nombre = nombres[num].strip().capitalize()
    nombres_normalizados.append(nombre)
    num+=1
print(nombres_normalizados)