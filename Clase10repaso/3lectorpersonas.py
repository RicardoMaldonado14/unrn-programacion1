personas = []
archivo = open("personas.csv", "r")

for persona in archivo.readlines()[1:]:
    nombre, apellido = persona.strip().split(",")
    personas.append({
        "nombre": nombre,
        "apellido": apellido
    })

archivo.close()
print(personas)