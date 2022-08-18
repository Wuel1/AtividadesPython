print('Olá ! Seja bem vindo a 2ª questão do Mini teste 3')
print('Digite uma sequência de 10 números inteiros')

numeros = []
numeros2 = []

for a in range(10):
    print('Digite o', a + 1 ,'valor:')
    n = int(input())
    numeros.append(n)

print('Agora digite outra sequência de 10 valores')

for a in range(10):
    print('Digite o', a + 1 ,'valor:')
    n = int(input())
    numeros2.append(n)

lista_final = numeros + numeros2
lista_final[::2] = numeros
lista_final[1::2] = numeros2
print('A primeira lista é:')
print(numeros)
print('A segunda lista é:')
print(numeros2)
print('A lista intercalada é',lista_final)

print('----------------------------------------------')
input('Aperte Enter para fechar o programa')
quit()
