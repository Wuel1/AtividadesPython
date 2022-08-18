input('Pressione alguma tecla para iniciar')
print('Olá ! Qual seu nome?')
nome = input()
print('Olá !',nome,'Seja bem-vindo!')

print('Digite dois números inteiros para o cálculo')
n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))

print('Agora digite qualquer número real')
n3 = float(input('Número real:'))

s1 = (n1*2) * (n2/2)
s2 = (n1*3) + n3
s3 = n3 ** 3

r1 = 'O produto do dobro do primeiro com metade do segundo é ' + str(s1)
r2 = 'A soma do triplo do primeiro com o terceiro é ' + str(s2)
r3 = 'O terceiro elevado ao cubo é ' + str(s3)

print(r1)
input('Aperte Enter para próxima operação')
print(r2)
input('Aperte Enter para próxima operação')
print(r3)
input('Aperte Enter para fechar o programa')
quit()
