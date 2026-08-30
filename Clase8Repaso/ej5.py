alumnos = [
 {
 "nombre": "Joaquin",
 "nota": 8,
 "materias": {"Programación", "Matemática"}
 },
 {
 "nombre": "Juan",
 "nota": 3,
 "materias": {"Programación"}
 },
 {
 "nombre": "Lucía",
 "nota": 9,
 "materias": {"Programación", "Inglés"}
 }
]
for alumno in alumnos:
    print(alumno["nombre"])

for alumno in alumnos:
    if alumno["nota"]>=7:
        print(f"el alumno: {alumno["nombre"]} aprobó")

for alumno in alumnos:
    if "Matemática" in alumno["materias"] :
        print(f"{alumno["nombre"]} cursa matematicas")

for alumno in alumnos:
    if alumno["nombre"] == "Joaquin":
        alumno["materias"].add("Laboratorio")
        print(f"las materias de {alumno["nombre"]} ahora son {alumno['materias']}")

    