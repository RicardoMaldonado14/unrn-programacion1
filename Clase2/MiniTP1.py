print("hola mundo")
nombre="Ricardo"
print("hola", nombre)
print(45*4)
print(80+594)
print((20**2)/10)
print(type((20**2)/10))
print(560.9/9)
print(1 + 2)
print(1 + 2.0)
print(10 // 3) #es una division entera, por lo que no tiene decimales
print(10 % 3) #es el resto de la operacion
#en el caso de tener solo un un parentesis el sistema dice SyntaxError: '(' was never closed
#en el caso d eno usar parentesis SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("en 42 minutos con 42 segundos hay", 42*60+42, "segundos")
mensaje="hola mundo!"
print(mensaje)
apellido="Maldonado"
print("Bienvenido", nombre, apellido, "al mundo Python")
caracter="aguante fuerza regida"
entero=540
flotante= 435.98
print(caracter, "es de tipo", type(caracter),
      entero, "es de tipo", type(entero), 
      flotante, "es de tipo", type(flotante))
ent1=321
flot1=126.53
print(ent1+flot1, type(ent1+flot1))
#programa de calculos de edad
print("cuantos años tiene?")
edad=int(input())
print("en base a su edad usted ha vivido", edad*12, "meses")
print("su edad en 10 anios será", edad+10, "anios")
print("ingrese su altura en cm")
altura=int(input())
print("el doble de tu altura es", altura*2)

#ejercicio Saludos
saludo="Hola richard "
print(saludo*3)
print("tu nombre tiene", len(nombre), "letras")

#parte 3
print("ingrese su nombre")
nombre1=input()
print("ingrese su edad")
edad1=input()
print("ingrese su altura en metros")
altura1=float(input())
programar=True
print("en que anio estamos?")
anio=input()
print("El alumno se llama", nombre1, "y tiene", anio, "anios",
      "mide", altura1, "le gusta programar? (si=1, no=0)", programar,
      "nació en el anio", anio-edad)