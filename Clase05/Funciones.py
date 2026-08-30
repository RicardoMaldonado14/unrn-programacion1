def saludar():
    print("hola")
saludar()

def bienvenida():
    nombre=input("ingrese su nombre: ")
    print(f"hola {nombre}")
    print("Bienvenido a mi programa🐢")

bienvenida()

#podemos pasarle un argumento a la funcion, esto se define dentro de los parentesis
#dentro de la funcion podemos utilizar los argumentos como si fueran variablesch
def saludo(nombre):
    print(f"hola {nombre}")

saludo("juan")


def saludo2(nombre1, nombre2):
    print(f"hola {nombre1} y {nombre2}")
saludo2("juan", "pedro")


#el retorno de una funcion nos permite devolver resultados al llamar a una funcion
#esto se hace con la palabra clave "return" y el contenido a retornar
print("retorno")
def saludo3(nombre3):
    return f"hola {nombre3}"
saludo3("juan")
print (saludo3("pedro"))