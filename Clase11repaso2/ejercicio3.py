def camel():
    frase = input("ingrese una frase: ")
    palabras = frase.split()
    palabrascamel = []
    for palabra in palabras:
        palabralimpia = palabra.strip().capitalize()
        palabrascamel.append(palabralimpia)
    frasecamel= " ".join(palabrascamel)
    return frasecamel


print(camel())