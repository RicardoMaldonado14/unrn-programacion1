#Dada una lista con nombres repetidos, mostrar:
#los nombres unicos
#la cantidad de nombres distintos
nombres=["ana", "juan", "ana", "pedro", "juan", "lucia"]
nombresunicos= set(nombres)
print(f"el conjunto de nombres es: {nombresunicos}, y tiene {len(nombresunicos)} nombres unicos")