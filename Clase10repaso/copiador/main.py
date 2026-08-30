archivo = open("copiador/entrada/frase.txt", "r")
contenido = archivo.read()
archivo.close()                                   

archivocopia = open("copiador/salida/frasecopia.txt", "w")
contenidocopia = archivocopia.write(contenido)
archivocopia.close()