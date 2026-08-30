#version hecha con IA gemini
def obtener_estado(nota):
    if nota >= 8:
        return "Promociona"
    elif nota >= 6: #en esta version se tienen en cuenta valores como 7.5
        # ya que en el mio 7.5 no es >= 8, y tampoco está en el rango entre 6 y 7
        return "Aprueba"
    else:
        return "Desaprueba"
# Pruebas con distintas notas
notas_de_prueba = [10, 8, 7, 6, 5, 2]


# notas_de_prueba = [10, 8, 7, 6, 5, 2]: Creamos una lista con los números que queremos testear.
# for n in notas_de_prueba:: Esto le dice a Python: "recorré la lista y, en cada vuelta, llamá n al número que sigue".
# resultado = obtener_estado(n): Adentro del bucle, le pasamos ese número n a tu función.
# print(f"Nota: {n} -> ..."): Usamos una f-string (la f antes de las comillas) para mostrar el número y el resultado de forma prolija.

for n in notas_de_prueba:
    resultado = obtener_estado(n)
    print(f"Nota: {n} -> Estado: {resultado}")
