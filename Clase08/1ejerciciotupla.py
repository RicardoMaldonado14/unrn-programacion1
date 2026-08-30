def persona (nombre, edad):
    return (nombre, edad, edad>18)


print(persona("lauti", 20))

#ejercicio con ia

def datospersona():
    nombre = "lauti"
    edad = 20
    condicion= edad>18
    return nombre, edad, condicion

resultado = datospersona()

print(resultado)

#version del profe
def datos(nombre1,edad1):
    mayoredad= False
    if edad1 >= 18:
        mayoredad= True
    return(nombre1, edad1, mayoredad)

