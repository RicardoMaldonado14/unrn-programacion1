#ejercicio 1
lista=["ricardo", "delfina", "fufi", "pochoclo"]
print(lista)
print(lista[0])
print(lista[-1])
print(len(lista))

lista_compras = ["pan", "leche", "huevos"]
print(lista_compras[0]) #devuelve "pan" ya que [0] es el primer elemento de la lista
print(lista_compras[-1]) #devuelve "huevos" ya que [-1] siempre devuelve el ultimo elemento de la lista
print(len(lista_compras)) #devuelve 4 ya que muestra la cantidad de elementos de la variable dentro de len()

# Ejercicio 3
# Escribir un programa que:
# Cree una lista vacia.
# Pida al usuario que ingrese un elemento.
# Agregue ese elemento a la lista.
# Repita el proceso hasta que el usuario escriba "fin".
# Al finalizar, mostrar:
# La lista completa.
# La cantidad de elementos ingresados.
print("arme su lista")
lista1=[]
while lista1!="finalizar":
    lista1.append(input("Agregue un elemento a la lista "))
print()