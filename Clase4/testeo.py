lista=[]
print(len(lista))
while len(lista)!=5:
    lista.append(input("agregue elementos a su lista: "))
    if len(lista)==5:
        print (lista)