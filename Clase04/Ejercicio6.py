# Ejercicio 6
# Escribir un programa que:
# Tenga una lista ya cargada.
# Pida al usuario un elemento.
# Indique si ese elemento esta en la lista.
# Si esta, mostrar en que posicion aparece.
lista=["muñe","fufi","nemo","pochoclo"]
mascota=input("ingrese una mascota: ")
for i in range(len(lista)):
    if mascota==lista[i]:
        print(f"la mascota es {mascota} y está en el lugar {i}")
        break
else:
    print("esa mascota no esta aca")