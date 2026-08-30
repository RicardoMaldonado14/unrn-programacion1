# Ejercicio 7 - Cargar nota de parcial
# Pedir al usuario una nota de parcial.
# Validar que:
# ● Sea numérica.
# ● Esté entre 0 y 10.
nota = input("ingrese nota del parcial: ")
if nota.strip().isnumeric():
    nota = int(nota)
    if 0<nota<=10:
        print(f"la nota es {nota}")
    else:
        print("nota fuera de rango")
else:
    print("formato de nota no esperado")