#listas de diccionarios

alumnos= [
    {"nombre": "paula", "nota": 8},
    {"nombre": "juan", "nota": 3},
    {"nombre": "pedro", "nota": 6}
]

alumnos.append (
    {"nombre": "jhon", "nota": 2}
)

for alumno in alumnos:
    if alumno["nota"]>=4:
        print(alumno["nombre"], "aprobo")
    else:
        print(alumno["nombre"],"desaprobado")
#un diccionario