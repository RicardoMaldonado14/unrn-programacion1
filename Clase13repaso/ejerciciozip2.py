llaves = ["id", "email", "age", "active"]
valores = [
 [1, "ana@mail.com", 28, True],
 [2, "luis@mail.com", 35, True],
 [3, "marcos@mail.com", 31, False],
 [4, "marta@mail.com", 25, True],
]

usuarios = []
for valor in valores:
    diccionario = dict(zip(llaves, valor))
    usuarios.append(diccionario)

for usuario in usuarios:
    print(usuario)  