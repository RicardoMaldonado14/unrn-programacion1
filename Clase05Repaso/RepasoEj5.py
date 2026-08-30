def obtener_estado(nota):
    if nota >= 8:
        return "promociona"
    elif nota < 6:
        return "desaprueba"
    else:
        return "aprueba"
    
calificacion=obtener_estado(int(input("---ingrese la nota del alumno: ")))
print (calificacion)


print("--Version de Gemini---")

def obtener_estado(nota):
    # Condición 1: Si la nota es 8, 9 o 10
    if nota >= 8:
        return "Promociona"
    # Condición 2: Si la nota es menor a 6 (0 al 5)
    elif nota < 6:
        return "Desaprueba"
    # Condición 3: Si no es ninguna de las anteriores, cae acá (notas 6 y 7)
    else:
        return "Aprueba"

# --- Pruebas automáticas con varias notas ---
print("--- Pruebas de control ---")
print(f"Nota 9: {obtener_estado(9)}")        # Debería decir Promociona
print(f"Nota 7: {obtener_estado(7)}")        # Debería decir Aprueba
print(f"Nota 4: {obtener_estado(4)}")        # Debería decir Desaprueba

print("\n--- Tu prueba interactiva ---")
# Tu línea original para que el usuario ingrese el dato por teclado
calificacion = obtener_estado(int(input("Ingrese la nota del alumno: ")))
print(f"El estado del alumno es: {calificacion}")
