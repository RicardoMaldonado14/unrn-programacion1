#estructura de datos que permite almacenar su contenido en forma d eclave valor
#nos permite construir de manera simple:
#dicha de alumno
#agenda d econtactos
#diccionario real, palabra -> definicion

diccionario= {
    "clave1" : "valor2",
    "clave2" : "valor2"
}
print(diccionario, type(diccionario))


print("-------------------")
#comparamos los casos de uso de una tupla vs un diccionario
alumnotupla= ("paula", "perez", 8)
print(alumnotupla[2])

alumnodict={
    "nombre":"paula",
    "apellido":"perez",
    "nota":8
}
print(alumnodict["nota"])


#Ejemplo:
#crear un diccionario
persona= {
    "nombre":"martin",
    "edad":20
}

#acceder a un valor usando su clave
print(persona["nombre"])

#modificar un vslor existente
persona["edad"]=21

#agregar nueva clave
persona["ciudad"]= "bariloche"

#preguntar si existe una clave
print("ciudad" in persona)

#obteniendo las keys
keys= persona.keys()

#obteniendo los values
values=persona.values()