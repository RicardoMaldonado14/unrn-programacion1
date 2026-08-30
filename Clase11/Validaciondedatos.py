#herramientas para validar
#la funcion isnumeric
print("1996".isnumeric())

#validando el tamaño de una entrada
len("1994")==4 #true
len(" 1994")==4 #false

#validando ingreso de palabras
"maria".isalpha() #true
"maria cecilia".isalpha() #false
#existe isalnum() valida que haya letras de A-Z y numeros sin espacio

#validando caracteres esperados
#cuendo esperamos el texto en cierto formato o separado por ","
# con count() o find()
# count() cuenta la cantidad de apariciones
"pedro, martinez, 19, 2004".count(",")==3 #true

