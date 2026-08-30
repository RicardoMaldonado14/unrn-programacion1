def pedircomida():
    comida=""
    while comida == "":
        comida = input("ingrese tu comida: ")
    return comida

def obtenerprecio(comida):
    precio=0
    if comida == "hamburguesa":
        precio = 100
    elif comida == "pizza":
        precio = 125
    elif comida == "milanesa":
        precio = 150

    if precio:
        print(f"comida {comida} - precio {precio}$")
    else: 
        print("no hay chau")
    return precio

total=0
while input("pedi comida gordo") != "terminar pedido":

    comida=pedircomida()
    total += obtenerprecio #FALTA COMPLETAR
    print(obtenerprecio(comida))