#las listas contienen varias variables
lista_de_super = [
    "Huevos",
    "Pan",
    "Coca",
    "Azucar", 
    "Leche",
    "Fideos"
]
print(type(lista_de_super))
print(lista_de_super)
lista_de_comida= ["pizza", "empanada", "hamburguesa"]
print(lista_de_comida)

# lista=[] es una lista vacia
#lista_textos=["ana", "pedro"]
#lista_numeros=[1, 2,  3]
#lista_flotantes=[1.1, 1.2]
print(len(lista_de_comida))
for indice in range(len(lista_de_comida)):
    #print(indice)
    #print(lista_de_comida[indice])
    print(f"{indice}:{lista_de_comida[indice]}")

indice=0
while indice < len(lista_de_comida):
    print(indice, lista_de_comida[indice])
    indice+=1
while True:
    indice_seleccionado=int(input("elegi la comida "))
    if indice_seleccionado < len(lista_de_comida):
        comida=lista_de_comida[indice_seleccionado]
        print(f"elegiste el indice {indice_seleccionado}:{comida}")
    else:
        print("elegiste una comida no valida")