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
elif pagamento == 3:
    print('Digite 1 para débito')
    print('Digite 2 para crédito')
    forma = int(input())
    if forma == 1:
        print('O valor a ser pago no débito é R$',valor_final,' Reais')
    elif forma == 2:
        print('Em quantas parcelas você deseja pagar?')
        parcelas = int(input())
        if parcelas > 3:
            print('Não aceitamos parcelas maiores que 3x, por favor tente novamente')
            input('Digite Enter para sair do programa')
            quit()
        else:
         valor_cartao = valor/parcelas
         print('O valor a ser pago em cartão é de R$',valor_final,'Reais. Dividido em',parcelas,' parcelas de R$',valor_cartao,' Reais')

input('Aperte Enter para sair do programa')
quit()

