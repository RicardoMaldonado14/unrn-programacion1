# Ejercicio 1
# Diseñar un algoritmo que determine si una persona puede entrar a un evento.
# Datos:
# edad
# tiene_documento (True o False)
# Condición:
# Solo puede entrar si tiene 18 años o más y tiene documento.
# Escribir los pasos en forma clara y ordenada.
edad=int(input("ingrese su edad: "))
documento=True
if edad>=18 and documento==True:
    print("podes pasar")
else:
    print("no podes pasar")
#se definen dos variables, una numerica(la edad) y una booleana (si tiene documento o no)
#si la edad es mayor o igual a 18, y ademas, el valor de la variable documento es True
#imprime el mensaje podes pasar.
#en caso de que una de las dos funciones no se cumpla imprime el mensaje "no podes pasar"

# Ejercicio 2
# Diseñar un algoritmo que indique qué ropa usar según la temperatura.
# Dato:
# temperatura
# Condiciones:
# Menor a 10: abrigo
# Entre 10 y 20: ropa media
# Mayor a 20: ropa liviana
temp=int(input("que temperatura hace? "))
if temp<10:
    print("lleva abrigo")
elif temp>20:
    print("lleva ropa liviana")
else:
    print("lleva ropa media")

#se le asigna un valor entero a la variable temp
#si temp<10 imprime en pantalla el mensaje "lleva abrigo"
#si no y temp>20 imprime el mensaje "lleva ropa liviana" 
#de lo contrario "lleva ropa media"

#Ejercicio 5
# Escribir un programa que determine si un número es:
# Par o impar
# Mayor, menor o igual a 10

numero=int(input("ingrese un numero: "))
if numero%2==1:
    print("el numero ingresado es impar")
elif numero%2==0:
    print("el numero es par")
par= numero*2
impar= numero*2+1
if numero<10:
    print("el numero ingresado es menor a 10")
elif numero>10:
    print("el numero ingresado es mayor a 10")
else:
    print("el numero ingresado es igual a 10")


# Ejercicio 6
# Sistema de acceso a un banco.
# Datos:
# clave_almacenada
# clave_ingresada
# usa_token (True o False)
# Condición:
# Permitir acceso si la clave es correcta o si se usa token.
# Mostrar uno de estos mensajes:
# Acceso permitido
# Acceso denegado
clave_alm="1234"
clave_ingr=int(input("ingrese su clave: "))
usa_token=False

if clave_ingr==clave_alm or usa_token==True:
    print("acceso  permitido")
else:
    print("acceso denegado")


#Ejercicio 7
#Se definen tres variables, una numerica (monto=900), y dos booleanas
#es_cliente_vip=False y tiene_cupon=True
#en base a estas variables, si el valor del monto es mayor a 1000 y el valor de 
# la variable cliente vip es verdadera se imprime en pantalla el mensaje "aplica descuento"
#este mensaje se imprime tambien si la variable tiene_cupon es verdadera (a pesar de que las otras dos no se cumplan)
#de lo contrario si las condiciones no se cumplen imprime en pantalla "no hay descuento"

# Ejercicio 8
# Usar un for para imprimir los números del 1 al 5.
for i in range(5):
    print(i+1)

#Ejercicio 9
print("la tabla del 2 es: ")
for i in range(1, 11):
    print(f"2 x {i} = {i*2}")

# Ejercicio 10
print("los dias de la semana son:")
dia="lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"
for i,dia in enumerate(dia):
    print(f"{i}: {dia}")