# Escribí un programa que:

# Pida al usuario el nombre de 4 alumnos.
# Valide que el nombre no esté vacío.
# Guarde los nombres válidos en una lista.
# Escriba los nombres en un archivo llamado alumnos.txt, un nombre por línea.
# Cierre el archivo.

listanombres = []

while len(listanombres)<4:
    nombre = input("ingrese 4 nombres: ")
    if nombre.strip() and nombre.isalpha() and len(nombre)>2:
        listanombres.append(nombre)
    else: 
        print("nombre no valido")
print(listanombres)

archivo = open("alumnos.txt", "w")
archivo.writelines("\n".join(listanombres))
archivo.close()