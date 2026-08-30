clave_alm="1234"
clave_ing=input("ingresar contraseña: ")
uso_clave_token=bool(input("usa clave token? SI/NO ") == "SI")

if clave_alm==clave_ing:
    print("acceso con clave")
elif uso_clave_token:
    print("acceso permitido")
else:
    print("acceso denegado")