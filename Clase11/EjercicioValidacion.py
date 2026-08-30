#Ejercicio 1 - Cargar nota del parcial
#pedir al usuario una nota, validar que sea numerica y que este entre 0 y 10

nota = 0
notamod = input("ingrese una nota: ")

if notamod.isnumeric() and int(notamod)>=0 and int(notamod)<=10:
    nota = int(notamod)
    print(f" la nota es: {nota}")
elif notamod.isnumeric()==False:
    print("ingrese una nota numerica")
else: 
    print("ingrese una nota dentro del rango 0-10")
