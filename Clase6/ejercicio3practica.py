x=[10, -1, 2, 3, 5, 7, 6, -7, 8, -10, 100]
#mostra el numero maximo y minimo
maximo=0
minimo=0
for i in x:
    if i>maximo:
        maximo=i
    elif i<minimo:
        minimo=i
        
print(f"el numero mas chico es {minimo}")
print(f"el numero mas grande es {maximo}")