lista = []
listafin = "fin"
elemento = input("ingrese un elemento: ").lower() 
while elemento!= listafin and len(lista)<5:
        lista.append(elemento)
        elemento = input("ingrese un elemento: ").lower() 
print(lista)
print(f"la cantidad de elementos mostrados es: {len(lista)} ")