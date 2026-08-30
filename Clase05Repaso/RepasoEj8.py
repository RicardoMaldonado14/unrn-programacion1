def pedido():
    comida = input("ingrese una comida: ")
    return comida

def precio(comida):
    if comida == "pizza":
        return 1600
    elif comida == "hamburguesa":
        return 1200
    elif comida == "milanesa":
        return 1000
    else:
        return 0
    
