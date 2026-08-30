# Ejercicio 7
# Armar un sistema simple de pedidos, el programa debe:
# Permitir agregar comidas a una lista.
# Aceptar solo estas opciones:
# pizza
# empanadas
# hamburguesa
# Si el usuario escribe otra opcion, mostrar un mensaje de error.
# Terminar cuando el usuario escriba "terminar".
# Al final:
# Mostrar el pedido completo.
# Mostrar cuantos elementos tiene el pedido.
comidas=["pizza", "empanada", "hamburguesa"]
opcion=""
pedido=[]
while opcion!="terminar":
    opcion=input("--ingrese su pedido: ")
    if opcion=="hamburguesa":
        pedido.append(opcion)
        print("perfecto, agregamos una hamburguesa a su pedido")
    if opcion=="pizza":
        pedido.append(opcion)
        print("perfecto, agregamos una pizza a su pedido")
    if opcion=="empanada":
        pedido.append(opcion)
        print("perfecto, agregamos una empanada a su pedido")
    elif opcion=="terminar":
        print(f"su pedido completo es {pedido} y tiene {len(pedido)} comidas")
    else:
        print(f"no tenemos {opcion}")
