```python
linea = " mara ; programacion ; 8 "

partes = linea.split(";")
nombre = partes[0].strip().capitalize()
materia = partes[1].strip().capitalize()
nota_texto = partes[2].strip()

if nota_texto.isnumeric():
    nota = int(nota_texto)
    print(f"{nombre} cursa {materia} y obtuvo {nota}")
else:
    print("La nota no es valida")
```
Para orientar la explicacion:
¿Que queda guardado en partes?
¿Por que se usa strip antes de capitalize?
¿Que dato se esta validando antes de convertirlo?
¿Que imprimiria el programa si en lugar de 8 viniera ocho?

    El codigo recibe una cadena de texto y la almacena en la variable linea, luego, con split
convierte la cadena de texto en una lista y la guarda en la variable "partes", para separar los
elementos de la lista usa como delimitador ";".
    Lo siguiente que hace el codigo es tomar el primer elemento de la lista "(partes[0])" para 
aplicarle la funcion strip() y capitalize() y lo guarda en la variable nombre, la funcion strip() 
debe estar primero ya que si fuera al revés (la funcion capitalize() antes de la funcion strip()), 
el programa "convertiria" en mayuscula un espacio vacio y luego lo eliminaria. Al estar en ese orden 
se evita este error, eliminando primero cualquier caracter no deseado y luego capitalizando el nombre.
    Ahora se toma el segundo elemento de la lista "partes[1]" y se le aplica las mismas funciones que
a "partes[1]", esta vez se guarda en la variable materias.
    Al  elemento "partes[2]", se le aplica la funcion strip ya que se espera que en esta posicion
se coloque un numero, este elemento se guarda en la variable nota_texto.
    En el siguiente paso se verifica que la variable nota_texto sea un numero, esto se consigue 
aplicandole la funcion isnumeric(), si esta condicion se cumple, la variable nota_texto se convierte
en un entero con int() y se guarda en la variable nota. Como paso final se imprime en pantalla un
mensaje personalizado con la estructura "{nombre} cursa {materia} y obtuvo {nota}".
    En caso de que no se cumpla la condicion nota_texto.isnumeric() se imprime en pantalla el 
mensaje "La nota no es valida".

