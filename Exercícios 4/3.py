numero = 1
mde3 = 0
print('Digite números inteiros')
while numero != 0:
    numero = int(input('-'))
    if numero % 3 == 0:
        mde3 += numero
    else:
        continue

print('A soma dos números multiplos de 3 informados é:', mde3)
input('Aperte Enter para fechar o programa')
