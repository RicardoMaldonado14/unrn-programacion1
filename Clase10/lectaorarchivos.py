archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.seek(5)
contvacio = archivo.read()

print("contenido: ", contenido)
print("contenido vacio: ", contvacio)

archivo.close()