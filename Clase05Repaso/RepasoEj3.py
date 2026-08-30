def es_par(num):
    paridad = num%2
    if paridad == 0:
        return True
    else:
        return False
    
print(es_par(3))
print(es_par(7))
print(es_par(10))


print("---Codigo optimizado por Gemini---")

# Definición de la función simplificada
def es_par(num):
    return num % 2 == 0

# Pruebas con 3 valores distintos
print(es_par(4))   # Devuelve True
print(es_par(11))  # Devuelve False
print(es_par(0))   # Devuelve True
