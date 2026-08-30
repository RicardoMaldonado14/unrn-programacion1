#Esta es una solucion alternativa al primer codigo mejorado con sugerencias de la ia
comidas=["pizza", "empanada", "hamburguesa"]
opcion=""
pedido=[]
while opcion!="terminar":
    opcion=input("--ingrese su pedido: ")
    if opcion in comidas:
        pedido.append(opcion)
        print(f"perfecto, agregamos {opcion} a su pedido")
    elif opcion=="terminar":
        print(f"su pedido completo es {pedido} y tiene {len(pedido)} comidas")
    else:
        print(f"no tenemos {opcion}")