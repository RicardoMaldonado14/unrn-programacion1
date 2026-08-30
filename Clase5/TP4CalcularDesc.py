def calcdesc(precio):
    if precio>10000:
        return precio-precio*0.1
    else:
        return precio
resultado= calcdesc(20000)

print(f"el precio final de su compra es: {resultado}")