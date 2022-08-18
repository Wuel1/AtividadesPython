print('Olá ! Informe 10 números inteiros')
numeros = []
soma = 0
lsoma = []
quadrados = 0
lquadrados = []

for a in range(10):
    n = int(input('-'))
    numeros.append(n)

for a in numeros:
    quadrados += a**2
    lquadrados.append(quadrados)
    soma += a
    lsoma.append(soma)

print('Os números informados são:')
print(numeros)
print('A soma dos quadrados dos números informados é:',quadrados)
print(lquadrados)
print('A soma dos números informados é:',soma)
print(lsoma)

input()
input('Digite Enter para fechar o programa')
quit()
