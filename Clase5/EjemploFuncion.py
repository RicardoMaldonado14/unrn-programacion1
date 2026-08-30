def trae_documento():
    return input("trae documento [si/no]: ") == "si"

def ingresar_edad():
    return int(input("ingrese su edad: "))

def puede_pasar(documento, edad):
    return documento == True and edad >= 18

documento=trae_documento()
edad=ingresar_edad()
if puede_pasar(documento, edad):
    print("puede pasar")
else: 
    print("no puede pasar")


def evaluar_energia(nivel=0):
    if nivel>7:
        print("modo mauina activado")
    elif nivel>4:
        print("se puede laburar")