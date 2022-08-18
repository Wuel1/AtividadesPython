print('Digite 10 Números:')
numeros = []
for a in range(10):
    n = int(input('Digite o número:'))
    numeros.append(n)

print(numeros[::-1])
input()
