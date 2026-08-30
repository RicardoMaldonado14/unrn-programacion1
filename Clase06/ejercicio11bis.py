lista = []
producto = input("ingrese un producto: ")
while producto != "fin":
    lista.append(producto)
    producto = input("ingrese un producto: ")

def funcion(argumento):
    print(f"la cantidad de elementos de su pedidos es: {len(argumento)}")
    prod_unicos = []
    for i in argumento:
        if i not in prod_unicos:
            prod_unicos.append(i)
    print(f"la lista de productos unicos es {prod_unicos}")

    for prod_uni in prod_unicos:
        contador = 0
        for prod in argumento:
            if prod == prod_uni:
                contador+=1
        print (f"{prod_uni} {contador}")


funcion(lista)