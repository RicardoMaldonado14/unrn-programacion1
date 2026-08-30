contraseña_registrada="1234"
contraseña_correcta = False
while contraseña_correcta == False:
    contraseña_ingresada = input("Ingresar contraseña: ")
    if contraseña_ingresada == contraseña_registrada:
        contraseña_correcta = True
print("Acceso permitido")

contraseña_ingresada = ""
while contraseña_ingresada != contraseña_registrada:
    contraseña_ingresada=input("Ingresar Contraseña")
print("acceso permitido otra vez jejejujujojo soy especial")

contador=1
while contador<=100:
    print(contador)
    contador = contador+1
    input("apreta enter para continuar")