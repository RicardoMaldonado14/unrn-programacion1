Verificaciones
1. Se pide verificar que un dato es un número?
RESPUESTA:
```python
if data.numeric():
    #codigo
```

2. Se pide verificar que tiene N cantidad de caracteres?
RESPUESTA:
```python
if len(dato) == 10:
    #se valida que el dato tenga 10 caracteres

if len(dato)>4:
    #se valida que tiene mas de 4 caracteres
```

3. Se pide verificar que no sea un dato vacío?
RESPUESTA:
```python
if len(dato)==0:
    #el dato esta vacio

if dato == "":
    #el dato esta vacio
```

4. Se pide verificar que un elemento más exista más de N veces?
RESPUESTA:
```python
datos = "nombre, edad, genero"
if datos.count(",")==2:
    #mi codigo
```

4. Si tenemos que verificar que un texto contenga otro texto?
RESPUESTA:
```python
#ejemplo para textos
dato="hola mundo"
if "hola" in dato:
    #el dato contiene hola

#ejemplo para listas
dato = ["minipimer"]
if "minipimer" in dato:
    #la lista contiene minipimer

#ejemplo diccionarios
dato= {"minipimer": {...}}
if "minipimer" in dato:
    #la clabe existe en el diccionario

#ejemplo para set
dato = {"minipimer"}
if "minipimer" in dato:
    #el valor existe en el conjunto
```



Repeticiones
1. Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?
RESPUESTA:
```python
datos = ["1", "2", "3"]

for dato in datos:
    if dato.isnumeric():
        #validamos que es dato
        int(dato)
```


2. Hay que pedirle 5 nombres al usuario. ¿Que hacemos?
RESPUESTA:
```python
datos = []
while len(datos)<5:
    datos.append(input("ingrese un nombre: "))

#ejemplo con for
datos =  []
for idx in range(5):
    datos.append(input("ingrese un nombre: "))
```


3. Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?
RESPUESTA:
```python
while true:
    userinput = input("ingrese un dato: ")
    if userinput == "fin":
        break


entrada = ""
while entrada != "fin":
    entrada = input("")


```

Archivos
1. Hay que leer un archivo:
RESPUESTA:
```python
f= open("Archivo.txt", "r")

#extraigo el texto
contenido = f.read()

#extraigo el texto separado por salto de lineas
contenidolista = f.readline()
```

2. Hay que escribir un archivo:
RESPUESTA:
```python
f.write("hola mundo")
f.close()

```
3. ¿Hay que cerrar un archivo?
RESPUESTA:
```python
f.close() #SIEMPRE tiene que estar si no podemos perder datos
```

Otros
1. Tenemos que solicitarle al usuario nombre, apellido y año de nacimiento ¿Que hacemos?
```python
nombre = input("ingrese un nombre: ")
apellido = input("ingrese el apellido: ")
anionacimiento = input("anio  que nacio ")
```

1.1 Tenemos que solicitarle al usuario que ingrese 25 nombres, apellidos y años de nacimiento ¿Que hacemos?
```python
datos = []
for idx in range(25):
    nombre = input("ingresar nombre: ")
    apellido = input("ingresar apellido: ")
    anionacimiento = input("año de nacimiento: ")
    {
        "nombre": nombre,
        "apellido": apellido,
        "anionacimiento": anionacimiento
    }
```


2. Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible.


