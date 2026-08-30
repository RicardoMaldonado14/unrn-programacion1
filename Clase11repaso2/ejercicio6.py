# Ejercicio 6 - Dando vuelta las palabras
# Definir una función que reciba una oración y devuelva la misma
# oración con el orden de las palabras invertido, sin usar split.
# Ejemplo: invertir_palabras("hola mundo python")
# Debe devolver: python mundo hola
def inversor(oracion):
    oracioninvertida= ""
    palabraactual = ""

    for caracter in oracion:
        if caracter != " ":
            palabraactual += caracter
        else:
            if palabraactual:
                if oracioninvertida:
                    oracioninvertida = palabraactual + " " + oracioninvertida
                else:
                    oracioninvertida = palabraactual
            palabraactual = ""

    if palabraactual:
        if oracioninvertida:
        
            oracioninvertida = palabraactual + "" + oracioninvertida
        else:
            oracioninvertida = palabraactual

    return oracioninvertida

resultado = inversor("me me me llamaron de colombia y yo lo ")

print(resultado)