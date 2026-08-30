pedido = []
condicion = True

while condicion:
    comida=input("ingrese una comida: ")
    if comida == "hamburguesa":
        pedido.append(comida)
        print("agregamos una hamburguesa")
    elif comida == "pizza":
        pedido.append(comida)
        print("agregamos una pizza")
    elif comida == "empanadas":
        pedido.append(comida)
        print("agregamos una empanadas")
    elif comida=="terminar": 
        condicion= False
    else: print("no tenemos esa comida")

print(f"su pedido completo es {pedido} y tiene {len(pedido)} comida/s")
