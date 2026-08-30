Explicá con tus palabras la diferencia entre:
Lista
Tupla
Conjunto
Diccionario
Para cada estructura, indicá un ejemplo de situación donde podría resultar útil.

Las listas son es una variable que permite tener mas de un valor dentro de esa sola variable
permite agrupar datos para: contarlos, agregarlos, eliminarlos, modificarlos.
Se definen con corchetes y los elementos se separan con comas.
Un ejemplo de uso es si le pido al usuario que ingrese datos hasta que se cumpla una condicion, puedo guardar
esos datos en una lista
```python
lista = []
valor = input("ingrese un valor: ")
while valor != "fin":
    lista.append(valor)
    valor = input("ingrese un valor: ")    
```

Las tuplas son parecidas a las listas, pero una vez creadas ya no se pueden modificar
Se definen con parentesis y los elementos se separan con comas.
Los elementos de la tupla pueden leerse y utilizarse en operaciones, PERO NO modificarse
un ejemplo de uso es si tengo una lista con datos, al convertirla en tupla  ya no se puede modificar
```python 
lista = [1, 2, 3, 4]
lista.append(3)
tupla= tuple(lista)
tupla.append(5) #el programa falla porque la tupla no permite agregar elementos
```

Un conjunto es una variable que permite almacenar muchos elementos y no los repite
puede aplicarse teoria de conjuntos (como en matematicas), union, interseccion y diferencia.
Se definen con llaves y los elementos se separan con comas.
Un ejemplo es convertir una lista a conjunto para eliminar los ementos repetidos
```python
lista = [1, 2, 2, 2, 3, 3, 4]
conjunto = set(lista)
print(conjunto)
```

Los diccionarios son estructuras que permiten almacenar datos con una clave y un valor para esa clave.
Se definen con llaves y a cada clave se le asigna un valor con :, luego se separan con comas
diccionario = {clave:valor}
un ejemplo de diccionario es si represento a una persona
```python
persona = {
    "nombre":"ricardo",
    "edad":20,
    "aprobado":True
}
print(persona["aprobado"])
```