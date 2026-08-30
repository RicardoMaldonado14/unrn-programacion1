def obtener_estado(nota):
    if nota>=8:
        return "promociona"
    elif 6<=nota<=7:
        return "aprueba"
    else:
        return "desaprueba"
    
print(obtener_estado(10))
