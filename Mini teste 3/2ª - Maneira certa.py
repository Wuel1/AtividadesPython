print('Aluno: Wandson Emanuel dos Santos Silva // Turma: EC2021.1')
input('--- Aperte Enter para iniciar o programa ---')
print('Olá ! Seja bem vindo a 2ª questão do Mini teste 3')
print('Digite uma sequência de 10 números inteiros')

lista = []
lista2 = []
lista_final = []
for a in range(10):
    print('Digite o', a + 1,'º valor:')
    n = int(input())
    lista.append(n)

print('Agora digite outra sequência de 10 valores')

for a in range(10):
    print('Digite o', a + 1,'º valor:')
    n = int(input())
    lista2.append(n)

for a in range(10):
    lista_final.append(lista[a])
    lista_final.append(lista2[a])

print('A lista com os primeiros valores informados:')
print(lista)
print('A lista com os segundos valores informados:')
print(lista2)
print('A lista com os valores intercalados:')
print(lista_final)

print('------------------------------------------------')
input('Digite Enter para fechar o programa')
quit()

