#ejercicio 1- normalizar datos de alumnos
#dada la siguiente lista mostrar cada alumno con el siguiente formato
# alumno'ana'-Notas:8-7-9

# lineas= [
#     "AnA;8;7;9",
#     "JuAn;4;5;3",
#     "LucIA;10;9;10"
# ]
 
# for linea in lineas:
#     partes = linea.split(";")
#     print(partes)
#     nombre = partes[0].lower()
#     print(nombre)

lineas= [
    "AnA;8;7;9",
     "JuAn;4;5;3",
     "LucIA;10;9;10"
]

nombres_limpios = []
for linea in lineas:
    print(linea)
    datos = linea.split(";")
    print(datos)
    nombresucio = datos[0]
    print(nombresucio)
    nombre = nombresucio.strip().capitalize()
    print(nombre)
    nombres_limpios.append(nombre)

print(nombres_limpios)


print("------------")


idx=0
for linea in lineas:
    datos = linea.split(";")
    notas = [datos[1], datos[2], datos[3]]
    notastxt = " - ".join(notas)
    print(notas, notastxt)
    print("")
    print(f"alumno '{nombres_limpios[idx]}' - Notas {notastxt}")
    idx+=1

