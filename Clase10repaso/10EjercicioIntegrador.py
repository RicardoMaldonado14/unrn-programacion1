listaalumnos= []
with open("10archivo.txt", "r") as archivo:
    contenido = archivo.readlines()

    for persona in contenido:
        nombre, notas = persona.strip().split(",")

        listanotas = []
        for nota in notas.split("-"):
            listanotas.append(int(nota))

        prom = sum(listanotas)/len(listanotas)
        print(f"el promedio de {nombre} es {prom}")
        diccionarioalumno={
            "nombre": nombre,
            "notas": notas,
            "promedio": prom
        }

        listaalumnos.append(diccionarioalumno)

for alumno in listaalumnos:
    print(alumno)

with open("10aprobados.txt", "w") as archivosalida:
    for alumno in listaalumnos:
        if alumno["promedio"]>=7:
            estado = "APRUEBA"
        else:
            estado = "DESAPRUEBA"
        linea = f"{alumno["nombre"]}, {alumno["promedio"]}, {estado}\n"
        archivosalida.write(linea)