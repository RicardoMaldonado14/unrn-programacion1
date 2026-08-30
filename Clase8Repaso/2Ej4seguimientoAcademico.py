# Se tiene una lista de diccionarios. Cada estudiante tiene:
# nombre,notas (lista de enteros), asistencias (cantidad), comision (string)
# Consignas
# Antes de empezar a escribir código, desarrollá una explicación completa de cómo resolverías el problema.
# Tomate el tiempo para pensar la estrategia, los pasos, las estructuras de datos y las decisiones lógicas. 
# Escribí ese análisis al comienzo del archivo, antes de la implementación.
# Mostrar promedio de cada estudiante.
# Clasificar cada estudiante en:
# Promociona si promedio >= 8 y asistencias >= 8
# Regulariza si promedio >= 4 y asistencias >= 6
# Recursa en otro caso
# Mostrar cuántos estudiantes hay en cada categoría.
# Mostrar la comisión con mejor promedio general.
# Generar un set con nombres de estudiantes en riesgo (Recursa).


estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6], "asistencias": 9, "comision": "C1"},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencias": 6, "comision": "C1"},
    {"nombre": "Mora", "notas": [9, 8, 10], "asistencias": 10, "comision": "C2"},
    {"nombre": "Pedro", "notas": [2, 4, 3], "asistencias": 7, "comision": "C2"}
]

print("---promedio de los estudiantes---")
for estudiante in estudiantes:
    promedio = sum(estudiante["notas"])/len(estudiante["notas"])
    print(f"el promedio de {estudiante["nombre"]} es {promedio}")

print("---promocion, regularizacion, recursada de estudiantes---")
diccionario =  {"promociona": 0, "regulariza": 0, "recursa": 0}
for estudiante in estudiantes:
    if sum(estudiante["notas"])/len(estudiante["notas"]) >= 8 and estudiante["asistencias"] >=8:
        print(f"{estudiante["nombre"]} promociona")
        diccionario["promociona"] +=1
    elif sum(estudiante["notas"])/len(estudiante["notas"]) >= 4 and estudiante["asistencias"] >=6:
        print(f"{estudiante["nombre"]} regulariza")
        diccionario["regulariza"] +=1
    else: 
        print(f"{estudiante["nombre"]} recursa")
        diccionario["recursa"] +=1
print(diccionario)

