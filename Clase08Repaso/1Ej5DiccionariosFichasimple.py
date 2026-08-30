# Crear un diccionario alumno con:
# nombre
# apellido
# edad
# Resolver:
# Mostrar nombre y apellido en una sola línea.
# Aumentar la edad en 1.
# Agregar la clave activo con valor True.
# Mostrar el diccionario completo.

alumno = {
    "nombre": "ricardo",
    "apellido": "maldonado",
    "edad": 20
}
print(alumno["nombre"], alumno["apellido"])
alumno["edad"] +=1
alumno["activo"] = True

print(alumno)