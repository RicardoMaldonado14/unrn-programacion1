lineas = [
" AnA ;8;7;9",
" JuAn ;4;5;3",
" LucIA ;10;9;10"
]

for alumno in lineas:
    datos = alumno.split(";")
    nombre = datos[0].strip().capitalize()
    notas = " - ".join(datos[1:])
    print(f"Alumno: {nombre} - Notas: {notas}")