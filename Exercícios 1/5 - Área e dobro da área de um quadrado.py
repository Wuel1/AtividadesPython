input('Pressione alguma tecla para iniciar')
print('Olá ! Qual seu nome?')
nome = input()
print('Olá !',nome,'Seja bem-vindo!')
print('Qual a base do quadrado?')
b = float(input())
print('Qual a altura do quadrado?')
h = float(input())
a = b * h
a2 = a * 2

area = 'A Área do quadrado é: ' + str(a)
area2 = 'O dobro da área do quadrado é: ' + str(a2)

print(area)
input('Digite Enter para saber o dobro da área')
print(area2)

input('Pressione a tecla Enter para fechar o programa')
quit()
