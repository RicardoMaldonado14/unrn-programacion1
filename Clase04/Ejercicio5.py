# Ejercicio 5
# Dada una lista, mostrar todos sus elementos usando while.
# Ejemplo:
# lista = ["pizza", "empanadas", "hamburguesa"]
# Salida esperada:
# 1. pizza
# 2. empanadas
# 3. hamburguesa
lista = ["pizza", "empanadas", "hamburguesa"]
i=0
while i<len(lista):
        print(f"{i}. {lista[i]}")
        i=i+1