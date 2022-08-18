input('Pressione alguma tecla para iniciar')

print('Olá ! Qual seu nome?')
nome = input()
print('Olá !',nome,'Seja bem vindo ao percentual online !')
print('Digite o número desejado:')
n1 = float(input())

print('Digite o percentual (sem ''%'') desejado:')
p1 = float(input())

perc = (p1 * n1)/100
resultado = str(p1) + '% de ' + str(n1) + ' é igual a: ' + str(perc)
print(resultado)

input('Pressione alguma tecla para fechar')
quit()

