usuarios = [
    "ana,programacion",
    "juan,matematica",
    "lucia,fisica"
]

listanombres=[]
listamaterias=[]
for linea in usuarios:
    dato = linea.split(",")
    print(dato)
    nombre = dato[0]
    print(nombre)
    nombremayus = nombre.capitalize()
    print(nombremayus)
    listanombres.append(nombremayus)
    materia = dato[1]
    materiamayus = materia.capitalize()
    listamaterias.append(materiamayus)


print(listanombres)
print(listamaterias)


