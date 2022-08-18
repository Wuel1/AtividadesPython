import math
input('Aperte a teclar Enter para iniciar o programa')
print('Olá ! Qual é seu nome?')
nome = input()
print('Olá,',nome,'! Seja bem-vindo a loja de tintas')
print('Informe em m² o tamanho da área a ser pintada: ')

m = float(input())

#1L de tinta equivale a 3 metros pintados // 1 lata tem 18L, logo 1 lata pinta 54m²
pl = 80.00
x = (m / 54)
dx = (math.ceil(x))
tl = dx
pla = dx * pl

if m <= 54:
    print('Você precisara apenas de 1 lata de tinta para pintar a área informada')
    print('O preço da lata é R$',pl,'Reais')
    input('Aperte Enter para sair do programa')
    quit()

if m > 54:
    print('Você precisará de',dx,'latas, para pintar a área informada')
    print('O preço de',dx,'latas é R$',pla,'Reais')
    input('Aperte Enter para sair do programa')
    quit()
        

