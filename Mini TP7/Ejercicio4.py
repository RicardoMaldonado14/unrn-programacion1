edad_ing = input("ingrese una edad: ").strip()
edadmin = 0
edadmax = 120
if edad_ing.isnumeric():
    edad = int(edad_ing)
    if edadmin < edad < edadmax:
        print(f"edad registrada: {edad}")
    else:
        print("ingrese unvalor dentro del rango")
else: 
    print("ingrese un valor numerico")