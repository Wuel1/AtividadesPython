input('Pressione alguma tecla para iniciar')
print('Olá ! Qual seu nome?')
nome = input()
print('Olá !',nome,'Seja bem-vindo!')
print(nome,'Quanto você ganha por hora?')

g1 = float(input('R$'))

print('Quantas horas por dia você trabalha?')
h = int(input())

t_dia = g1 * h
tdu = t_dia * 22
dia_sabado = (h/2) * g1
t = tdu + dia_sabado

resultado = 'Trabalhando ' + str(h) + ' horas por dia,você ganha: R$' + str(t) + ' no mês.' 

print(resultado)

input('Pressione a tecla Enter para fechar o programa')
quit()
