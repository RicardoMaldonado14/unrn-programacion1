print("retorno")
def saludo3(nombre3):
    return f"hola {nombre3}"
print(saludo3("juan"))

saludo=saludo3("pepin")
print(saludo)

def sumar(a, b):
    return a+b
resultado=sumar(1, 2)
print(resultado)

def mayor(edad):
    if edad >= 18:
        return True
    else:
        return False
    
print(mayor(15))
print(mayor(20))