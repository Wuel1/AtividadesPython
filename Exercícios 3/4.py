print('Digite 5 números e veja qual é o maior:')
numeros = []

for a in range(5):
    n = float(input('Digite o número:'))
    numeros.append(n)

print(numeros)
print('O número máximo é',max(numeros))

input()
input()
quit()
