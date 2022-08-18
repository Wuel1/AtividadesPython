lista = list(range(1,1001))
contador = 0
d5 = 0
d7 = 0
d10 = 0 
for i in lista:
    if i % 5 == 0:
        contador += 1
        d5 += 1
    elif i % 7 == 0:
        contador += 1
        d7 += 1
    elif i % 10 == 0:
        contador += 1
        d10 += 1


print(contador)
print(d5)
print(d7)
print(d10)
