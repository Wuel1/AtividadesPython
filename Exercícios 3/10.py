print('Digite 10 números')

numeros = []
numeros_pares = 0
numeros_impares = 0

for a in range(10):
    n = int(input('Digite o número:'))
    numeros.append(n)

for b in numeros:
    if b % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print('A sua lista digitada foi:')
print(numeros)
print('Nessa lista temos', numeros_pares,' números pares')
print('Nessa lista temos', numeros_impares,' números impares')

input()
quit()
