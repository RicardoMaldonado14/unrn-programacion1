import RepasoEj8 
pedidocomida= RepasoEj8.pedido()
if pedidocomida in ["pizza", "hamburguesa", "milanesa"]:
    valor= RepasoEj8.precio(pedidocomida)
    print(f"la comida elegida es {pedidocomida} y vale ${valor}")
else:
    print ("esa comida no esta en el menu")