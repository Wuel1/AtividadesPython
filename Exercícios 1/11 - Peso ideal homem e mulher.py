import math
input('Aperte Enter para iniciar o programa')
nome = input('Olá ! Qual seu nome? ')
print('Olá',nome,'Seja bem-vindo !')

h = float(input('Qual a sua altura? '))

ph = (72.7*h) - 58
pm = (62.1*h) - 44.7
ph1 = math.ceil(int(ph))
pm1 = math.ceil(int(pm))

resultado1 = 'Se você for homem, seu peso ideal é: ' + str(ph1) + 'kg'
resultado2 = 'Se você for mulher, seu peso ideal é: ' + str(pm1) + 'kg'

print(resultado1)
print(resultado2)

input('Aperte Enter para fechar o programa')
quit()
