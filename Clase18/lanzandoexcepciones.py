def sumador(anterior, siguiente):
    if siguiente<anterior:
        raise ValueError(f"el numero siguiente no puede ser mas chico que el anterior")
    else:
        return siguiente+anterior


anterior_n = 0
while True:
    print(f"el numero anterior es {anterior_n}")
    try:
        siguiente_n = int(input("ingrese el siguiente numero"))
    except:
        pass

        
        sumador(anterior_n, siguiente_n)
        anterior_n = siguiente_n
    except ValueError as error:
        if "invalid literal" in str(error):
            print("int valido")
        elif "el numero siguiente" in str(error):



sumador(13,1)