#ejercicio 1
comandos = [" ENCENDER ", "apagar", " Estado ", "REINICIAR", " salir "]

normalizados = [comando.strip().capitalize() for comando in comandos ]
print (normalizados)

#ejercicio 2
notas = [2, 4, 6, 8, 10, 3, 7, 9]


listallena = [True if nota>=6 else False for nota in notas  ]

print(listallena)

#ejercicio 3 transformar en una lista mediante comprensions
mediciones = [3.2, 2.8, 4.1, 5.5, 3.0, 6.2, 4.8]
e = [valor for valor in mediciones if valor < 3.0 or valor > 5.0 ]
print(e)