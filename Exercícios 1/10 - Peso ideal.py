input('Pressione alguma tecla para iniciar')
print('Olá ! Qual seu nome?')
nome = input()
print('Olá !',nome,'Seja bem-vindo!')

print(nome,'Informe sua altura em metros')
h = float(input())

pi = (72.7*h) - 58
piint = int(pi)

resultado = str(nome) + ' seu peso ideal para sua altura é de: ' + str(piint)+ 'kg'

print(resultado)
input('Aperte Enter para sair do programa')
quit ()
