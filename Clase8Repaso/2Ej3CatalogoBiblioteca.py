# Tenés una lista de libros, donde cada libro está representado por una tupla: (titulo, autor, anio, genero).
# Mostrar todos los títulos publicados después de 2010.
# Obtener un set con los géneros disponibles.
# Crear un diccionario donde la clave sea el género y el valor la cantidad de libros de ese género.
# Mostrar qué género tiene más libros.
# Mostrar los géneros sin repetirse.

libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]

print("---Los libros publicados despues de 2010 son: ")
for libro in libros:
    if libro[2]>2010:
        print(libro[0])

generos = []
for libro in libros:
    generos.append(libro[3])
setgeneros = set(generos)


diccionario = {}
for genero in generos:
    if genero not in diccionario:
        diccionario[genero] = 1
    else:
        diccionario[genero] += 1


generomax = ""
librosmax = 0
for genero, cantidad in diccionario.items():
    if cantidad > librosmax:
        librosmax = cantidad
        generomax = genero

print(f"los generos disponibles son {setgeneros}")
print(f"el genero {generomax} es el que mas libros tiene, con un total de {librosmax} libros")
print("los generos sin repetirse son: ")
for i in setgeneros:
    print(i)
