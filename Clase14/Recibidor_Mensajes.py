import cliente
import cowsay


while True:
    msg = cliente.obtener_mensaje()
    if msg == None:
        continue
    msg_formateado= f"{msg["usuario"]}:{msg["texto"]}"
    print(cowsay.tux(msg_formateado))
    print(type(msg))