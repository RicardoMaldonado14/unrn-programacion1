lista=[""]
while lista[-1] != "fin":
    lista.append(input("agregue elementos a su lista: "))
if lista[-1] == "fin":
    lista.remove("fin")
    lista.remove("")
print(f"su lista completa es: {lista}")
print(f"su lista tiene {len(lista)} elementos")
