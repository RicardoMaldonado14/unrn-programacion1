salir=True
i = 0 
while salir:
    print(f"hola es la iteracion {i+1}")
    i+=1
    if input("continuar? [si/no]") == "si":
        #salir=False
        #break
        continue
    if input("desea salir? [si/no]") =="si":
        #salir=False
        break
    print(f"anashe, esta es la iteración: {i-1}")
print("adios")