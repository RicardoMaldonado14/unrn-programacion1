contra_alm=input("contraseña almacenada: ")
contra_ingresada=input("ingresar contraseña: ")
acceso_permitido=False

if contra_ingresada==contra_alm:
    acceso_permitido=True
    print("Acceso permitido")
if contra_ingresada!=contra_alm:
    acceso_permitido=False
    print("acceso denegado")
print("gracias por usar el sitema")