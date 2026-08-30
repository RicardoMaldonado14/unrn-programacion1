# notas = [4, 7, 5, 9, 6]
# # Con comprensión
# estados = ["Aprobado" if n >= 6 else "Desaprobado" for n in notas]
# # Con for
# estados = []
# for nota in notas:
#     if nota >= 6:
#        estados.append("Aprobado")
#     else:
#         estados.append("Desaprobado")
comandos = [" ENCENDER ", "apagar", " Estado ", "REINICIAR", " salir "]

normalizados = [comando.strip().capitalize() for comando in comandos]

notas = [2, 4, 6, 8, 10, 3, 7, 9]

estado = [True if nota>=6 else False for nota in notas]
#estado = [nota >= 6 for nota in notas]
# nota >= 6 ya devuelve por sí misma un valor booleano (True o False),
# no hace falta usar la estructura True if ... else False.
print(estado)

mediciones = [3.2, 2.8, 4.1, 5.5, 3.0, 6.2, 4.8]
fueraderango = [valor for valor in mediciones if valor < 3.0 or valor > 5.0 ]
print(fueraderango)