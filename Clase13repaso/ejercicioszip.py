productos = ["mouse", "teclado", "monitor", "notebook"]
stock_ayer = [10, 5, 3, 2]
stock_hoy = [7, 8, 3, 1]

for producto, stockayer, stockhoy in zip(productos, stock_ayer, stock_hoy):
    diferencia = stockayer-stockhoy
    print(f"el producto {producto} ayer tenia {stockayer} y hoy tiene {stockhoy}\
 hay una cambio de: {diferencia}")