archivo = open("7texto.txt", "w")
datos = ["hola", "soy", "richard\n", ":D"]

archivo.writelines(datos)

archivo.close()