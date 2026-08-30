#el for nos permite realizar repeticiones N cantidad de veces
#repetir 100 veces Hola
for _ in range(0,100): #acordarse de poner los espacios entre el for y el guion bajok
    print("hola")

#si quisieramos ver cuantas personas saludamos lo expresamos de la siguiente manera
for i in range(0,100):
    print("hola"+str(i+1))
#con for podemos ejecutar codigo, es decir poner condicionales y variables
for alumno in range (0, 30):
    alumno_id=alumno+1
    if (alumno%2):
        print(f"alumno {alumno_id} aprobado")
    else:
        print(f"alumno {alumno_id} desaprobado")

range(5)
range(1, 5)
range(-10, 0)
range(0, 10, 2)
range(0, 10, -1)