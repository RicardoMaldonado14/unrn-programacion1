mascotas = ["muñe", "fufi", "nemo", "pochoclo"]
elemento=input("ingrese un elemento: ")
i=0
encontrado=False

while i<len(mascotas):
    if mascotas[i]==elemento:    
        print(i, elemento)
        encontrado=True
    i +=1
if encontrado== False:
    print("no esta en la lista")