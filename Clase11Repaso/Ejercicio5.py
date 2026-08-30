# Pedir al usuario un codigo de materia con este formato:
# PROG-101
# El programa tiene que validar que:
# tenga un solo guion -;
# la parte de la izquierda tenga solo letras;
# la parte de la derecha tenga solo numeros.
# Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo upper).
# Ejemplo:
# Codigo valido: PROG-101
codigo = input("ingrese un codigo con el formato PROG-101: ")
if codigo.count("-")==1:
    listacodigo = codigo.split("-")
    if listacodigo[0].strip().isalpha() and listacodigo[1].strip().isnumeric():
        codigoletras= listacodigo[0].strip().upper()
        codigonumero= listacodigo[1].strip()
        print("codigo valido")
        print(f"{codigoletras}-{codigonumero}")
    else:
        print("formato de codigo no valido")
else:
    print("formato de codigo no valido, debe tener un guion")