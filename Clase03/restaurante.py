opcion = ""
precio = 0
print("Selecciona la comida para llevar")
while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: ").lower()
    if opcion == "pizza":
        precio= precio+50
        print("Excelente! Agregamos una pizza a tu pedido")
    if opcion == "hamburguesa":
        precio= precio+30
        print("Excelente! Agregamos una hamburguesa a tu pedido")
    if opcion == "empanadas":
        precio= precio+40
        print("Excelente! Agregamos empanadas a tu pedido")
    elif opcion == "terminar pedido":
        print("cerrando pedido...")
    else:
        print(f"lo siento, no tenemos {opcion}, prueba con otra cosa)")
print(f"Pedido finalizado, su total es de {precio} pesos gracias por confiar en nosotros")