resultado= ""
lista=[]
while resultado != "fin":
    resultado=input("agregar a su lista ")
    if resultado != "fin":
        lista.append(resultado)
    if len(lista)==5:
        break
print(f"su lista es {lista}")
print(f"su lista tiene {len(lista)} elementos")
