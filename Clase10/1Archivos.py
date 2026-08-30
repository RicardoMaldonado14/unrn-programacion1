#repaso clase 8:
#tuplas
#
#conjuntos: no son ordenados, sirven para hacer busquedas rapidas, son modificables
#en su mayoria los vamos a usar para pasarles una lista y ver los elementos unicos de la misma

#manejo de archivos:
#Lectura de archivos

#crear archivo datos.txt
#crear lector_archivos.py


#mecanismo de lectura de archivos
#para leer archivos usamos:
#   open(NOMBRE_ARCHIVO, "r") la r de read

#leyendo linea a linea
archivo = open("datos.txt", "r")
#lee el archivo hasta encontrar una linea completa delimitada por ?n
linea = archivo.readline()
print(linea.strip)

#volcando el archivo a una lista
archivo= open("datos.txt", "r")

#lee el archivo y lo vuelca linea a linea en una lista
lineas = archivo.readlines()
print(lineas)

#operando los datos de un archivo
#hacer un archivo numeros.txt

#mostrador de numeros.py
numeros = []
archivo = open("numeros.txt", "r")
for numero in archivo.readlines():
    numeros.append(int(numero))
archivo.close()

print(sum(numeros))

#podemos pasar de una archivo de texto plano a una estructura de datos dentro de nuestro programa

#personas.csv
#nombre, apellido
#juan, carlos

#lector de base de datso

personas=[]
archivo = open("personas.csv", "r")
for persona in archivo.readlines()[1:]:
    nombre, apellido = persona.strip().split(",")
    personas.append({
        "nombre": nombre,
        "apellido": apellido
    })

archivo.close()
print(personas)

