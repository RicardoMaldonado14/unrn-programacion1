alumnos = [
    {
        "nombre": "joaquin",
        "nota":[8, 5, 2], 
        "materias": {"programacion", "matematicas"}
    },
    {
        "nombre": "juan",
        "nota":[7, 9, 9], 
        "materias": {"programacion"}
    },
    {
        "nombre": "lucia",
        "nota":[4, 7, 9], 
        "materias": {"programacion", "ingles"}
    }
]
for alumno in alumnos:
    print(f"los alumnos son: {alumno["nombre"]}")
    

for alumno in alumnos:
    promedio= sum(alumno["nota"])/len(alumno["nota"])
    if promedio>=4:
        print (f"{alumno["nombre"]} aprobo")

for alumno in alumnos:
    if "matematicas" in alumno["materias"]:
        print(f"{alumno["nombre"]} esta en matematicas")

alumnos[0]["materias"].add("laboratorio")
print(alumnos[0])