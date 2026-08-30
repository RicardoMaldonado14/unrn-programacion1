# Un programa recibe comandos escritos por
# usuario:
# " encender "
# "APAGAR"
# " estado "
# "reiniciar"
# Hay que normalizarlos y aceptar solo: encender,
# apagar, estado.
comandos = ["encender", "apagar", "estado"]
comando = input("ingrese un estado: ").strip().lower()
if comando in comandos:
    print("comando aceptado")
else:
    print("comando rechazado")