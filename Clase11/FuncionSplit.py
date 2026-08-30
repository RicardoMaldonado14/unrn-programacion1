#Funcion Split
print("ana; 8; 7; 9".split(";"))
# string.split(delimitador, MAXSPLIT=-1) es la cantidad de veces que se divide una cosa 
# segun el caracter elegido, por defecto el valor que tiene es -1 (infinito)

print("ana; 8; 7; 9".split(";", maxsplit=2))

#funcion strip
#elimina caracteres vacios en los bordes
#string.strip(characters=none)
print(" hola mundo ".strip())
print("$hola mundo$".strip("$"))
print("$hola mundo$+".strip("$"))

#Funcion Capitalize
#Hace que el primer caracter del texto sea mayuscula y el resto minuscula.
#"HOLA".capitalize()
#" HOLA".capitalize()
print("HOLA".capitalize())
print(" HOLA".capitalize())

#Funcion join
#nos permite unir letrs de strings
#string.join(lista)
print(" ".join(["Soy", "un", "programador"]))
print("\n".join(["Soy", "un", "programador"]))


#slicing de listas
#sintaxis [inicio:fin:paso]


