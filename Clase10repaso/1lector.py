archivo = open("texto.txt", "r")
contenido = archivo.read()
contenidovacio = archivo.read()
print("contenido: ", contenido)
print("contenido vacio: ", contenidovacio)

archivo.close()

#para leer de vuelta el archivo uso el punto seek(0)
archivo = open("texto.txt", "r")
contenido = archivo.read()
archivo.seek(0)
contenidodevuelta = archivo.read()
print("contenido: ", contenido)
print("contenido vacio: ", contenidodevuelta)

archivo.close()
