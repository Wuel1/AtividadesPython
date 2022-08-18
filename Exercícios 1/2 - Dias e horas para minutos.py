input('Pressione a tecla enter para iniciar o programa')
print('Digite o seu nome')

nome = input()

print('Olá,',nome,'Seja bem-vindo !')

print('Quantos dias?')

d = int(input())

dm = (d * 24) * 60

print('Quantas horas?')

h = int(input())

hm = h * 60

print('Quantos minutos?')

m = int(input())

tm = dm + hm + m

resultado = 'Já se passaram '+ str(tm) + ' minutos'

print(resultado)

input('Digite enter para encerrar o programa')
quit()
