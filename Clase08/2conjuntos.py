conjunto = {1, 2, 3, 3, 4}
print(conjunto)
print(len(conjunto))
print(type(conjunto))

#agregar con add
conjunto.add ("lucia")
print (conjunto)

#eliminar con remove
conjunto.remove(2)
print(conjunto)

#consultar pertenencia con in
print("ana" in conjunto)

#convertir lista a set para eliminar repetidos
listanombres= ["ana", "juan", "ana", "pedro"]
nombresunicos=set(listanombres)
print(nombresunicos)

#se puede aplicar teoria de conjuntos


print("---APLICACION TEORIA DE CONJUNTOS")
#sets: union interseccion y diferencia
a= {"ana", "juan", "pedro"}
b= {"juan", "lucia"}

print("grupo A:", a)
print("grupo B:", b)

#union: junta los elementos de ambors grupos
print("Union: ", a|b)

#interseccion: muestra los elementos que tienen en comun
print("interseccion: ", a&b)

#diferencia: muestra que elementos estan en A pero no en B
print("Diferencia: ", a-b)