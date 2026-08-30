mascotas = ["muñe", "fufi", "nemo", "pochoclo"]
elemento = str(input("ingrese un elemento: "))

if elemento in mascotas:
    indice = mascotas.index(elemento)
    print("la mascota esta en el lugar", indice+1)
else: print("no esta en la lista papito")
