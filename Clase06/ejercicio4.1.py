nums = [1, 2, 2, 3, 4, 4, 4, 5]
lista=[]
for i in nums:
    if i not in lista:
        lista.append(i)

print(lista)