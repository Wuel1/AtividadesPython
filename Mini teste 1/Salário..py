print('- Seja bem-vindo ao Mini teste de programação do aluno Wandson Emanuel -')
input('Aperte Enter para continuar')
print('Qual seu nome?')
nome = input()
print('Olá',nome,'!')

print(nome,', quanto você ganha por hora trabalhada?')

GHtrabalhada = float(input('R$'))

print(nome,', quantas horas você trabalha por mês?')

Htrabalhada_mes = float(input())

salario = GHtrabalhada * Htrabalhada_mes

resultado = str(nome) + ', o seu salário bruto por mês é de: R$ ' + str(salario) + ' Reais.'

print(resultado)
input('Aperte Enter para fechar o programa')
quit()
