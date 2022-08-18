import math
input('Aperte a teclar Enter para iniciar o programa')
print('Olá ! Qual é seu nome?')
nome = input()
print('Olá,',nome,'! Seja bem-vindo a loja de tintas')
print('Informe em m² o tamanho da área a ser pintada: ')

m = float(input())

#1L de tinta equivale a 3 metros pintados
#1 lata de 18L pinta 54m²
#1 lata de 3.6L Pinta 10.8m²
pl = 80.00
p2 = 25.00
m10 = (m*110) / 100
x1 = (m / 54)
x2 = (m / 10.8)
x3 = (m10 / 54)
x4 = (m10 / 10.8)
dx1 = (math.ceil(x1))
dx2 = (math.ceil(x2))
dx3 = (math.ceil(x3))
dx4 = (math.ceil(x4))
pla1 = dx1 * pl
pla2 = dx2 * p2
pla3 = dx3 * pl
pla4 = dx4 * p2
l1 = '18 litros'
l2 = '3.6 litros'

z = input('Você deseja comprar apenas com latas de 18 litros? sim / não ')
if z == 'sim':
    print('Você precisará de',dx1,'latas')
    print('O valor será de R$',pla1,'Reais')

z1 = input('Você deseja comprar apenas com galões de 3.6 litros? sim / não ')
if z1 == 'sim':
    print('Você precisará de',dx2,'latas')
    print('O valor será de R$',pla2,'Reais')

z2 = input('Você deseja ver qual o melhor custo benefício entre latas e galões? sim / não ')
if z2 == 'sim':
    if pla3 < pla4:
        print('O melhor custo benefício é comprar,',dx3,'latas de',l1,'(Contando com os 10% de segurança)')
        print('O valor será de R$',pla3,' Reais')
    if pla4 < pla3:
        print('O melhor custo benefício é comprar,',dx4,'latas de',l2,'(Contando com os 10% de segurança)')
        print('O valor será de R$',pla4,' Reais')

input('Aperte Enter para sair do programa')
quit()
