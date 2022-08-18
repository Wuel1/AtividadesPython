print('Olá ! Seja bem vindo a 2ª questão do Mini teste 3')
print('Digite uma sequência de 10 números inteiros')

numeros = []
numeros2 = []
numeros3 = []
for a in range(2):
    print('Digite o', a + 1 ,'valor:')
    n = int(input())
    numeros.append(n)

print('Agora digite outra sequência de 10 valores')

for a in range(2):
    print('Digite o', a + 1 ,'valor:')
    n = int(input())
    numeros2.append(n)

for a in range(2):
    numeros3.append(numeros[a])
    numeros3.append(numeros2[a])

print(numeros3)
