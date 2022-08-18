input('Aperte Enter para Iniciar o programa')
print('Qual seu nome?')
nome = input()
print('Olá,',nome,'Seja bem vindo !')
print('Qual valor do produto comprado?')
valor = float(input())
print('Forma de pagamento:')
print('Digite 1 para Dinheiro')
print('Digite 2 para Cheque')
print('Digite 3 para Cartão')
pagamento = int(input())

if valor >= 100.0 and pagamento == 1:
    desconto = (valor*10)/100
else:
    desconto = 0

valor_final = valor - desconto

if pagamento == 2:
    print('O valor a ser pago em cheque é R$',valor_final,' Reais')
elif pagamento == 1:
    print('O valor a ser pago em dinheiro é R$',valor_final,' Reais')
else:
    print('Forma de pagamento inválida')

input('Aperte Enter para sair do programa')
quit()

