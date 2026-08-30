#este ejercicio igual fue mejorado con ayuda de ia
lista=["muñe","fufi","nemo","pochoclo"]
mascota=input("ingrese una mascota: ")
i=0
encontrado=False
while i<len(lista):
    if lista[i]==mascota:
        print(f"{mascota} esta en el lugar {i}")
        encontrado=True
    i+=1
if encontrado==False:
        print("esa mascota no esta")