usuarios = [
"ana,programacion",
"juan,matematica",
"lucia,fisica"
]

for usuario in usuarios:
    datos = usuario.split(",")
    nombre = datos[0].capitalize()
    materia = datos[1].capitalize()
    print(f"Hola {nombre}, estas inscripto/a en {materia}")