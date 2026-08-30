#json son tipos de archivos escritos de tal manera que piueden leerlos 
#programas hechos en distintks lenguajes, es un estandar

#formato JSON
#   llaves {} para objetos
#   corchetes [] para arrays (son listas o tuplas)
#   las claves van entre comillas dobles

#equivalencias de python a JSON
#   pyhton|JSON
#   dict | object
#   list | array
#   none | null
#   true/false|true/false

#escribir JSON desde python
import json
producto= {
    "nombre": "coca",
    "precio": 950,
    "stock": 9
}

with open("producto.json", "w") as archivo:
    json.dump(producto, archivo)