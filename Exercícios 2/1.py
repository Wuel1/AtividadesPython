input('Olá ! Aperte Enter para iniciar o programa')
print('Qual é seu nome?')
nome = input()
print('Olá',nome,', Seja bem vindo !')
print('digite o valor:')
valor = float(input())

positivo = valor > 0
negativo = valor < 0
neutro = valor == 0

if positivo == True:
    print('O valor informado',valor,', é positivo !')
elif negativo == True:
    print('O valor informado',valor,', é negativo !')
elif neutro == True:
    print('O valor informado',valor,', é neutro !')

input('Aperte Enter para fechar o programa')
quit()
