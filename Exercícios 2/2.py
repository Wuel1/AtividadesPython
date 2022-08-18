input('Olá ! Aperte Enter para iniciar o programa')
print('Qual é seu nome?')
nome = input()
print('Olá',nome,', Seja bem vindo !')
print('digite o valor:')
valor = float(input())

impar = valor%2 == 1

if impar == True:
    print('Este valor é Impar')
else:
    print('Este valor é par')
    
input('Aperte Enter para fechar o programa')
quit()
