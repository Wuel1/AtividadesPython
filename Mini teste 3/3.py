print('Aluno: Wandson Emanuel dos Santos Silva // EC2021.1')
print('Olá ! Seja bem-vindo a 3 questão do mini teste 3')
input('----------Aperte ENTER para iniciar o programa--------')

print('Seja bem vindo a lavanderia UABJ')

peça = 0
quilo = 0
contador_seco = 0
lista_valores = []

for a in range(5):
    x = 0
    print('Digite 1 para ser cobrado por peça de roupa. // Valor: R$7,00')
    print('Digite 2 para ser cobrado por quilo. // Valor: R$5,00')
    while x < 1:
        opçao = int(input('-'))
        if opçao == 1:
            preço = 7.00
            x += 1
            print('Quantas peças você deseja lavar?')
            qt_peças = int(input('-'))
            peça += qt_peças
            valor = (preço * qt_peças)
            print('Você deseja fazer a lavagem a seco? Caso sim, o valor será acrescentado em R$3.50')
            print('Digite 1 para SIM // Digite 2 para NÃO')
            seco = int(input('-'))
            if seco == 1:
                valor += 3.50
                contador_seco += 1
                lista_valores.append(valor)
                print('Pedido confirmado ! Cobrado por peça //',qt_peças,' peças // Lavagem a seco Preço Final R$',valor)
            else:
                lista_valores.append(valor)
                print('Pedido confirmado ! Cobrado por peça //',qt_peças,' peças // SEM lavagem a seco Preço Final R$',valor)
                
        elif opçao == 2:
            preço = 5.00
            x += 1
            print('Quantaos quilos você deseja lavar?')
            qt_quilos = int(input('-'))
            quilo += qt_quilos
            valor = (preço * qt_quilos)
            print('Você deseja fazer a lavagem a seco? Caso sim, o valor será acrescentado em R$3.50')
            print('Digite 1 para SIM // Digite 2 para NÃO')
            seco = int(input('-'))
            if seco == 1:
                valor += 3.50
                contador_seco += 1
                lista_valores.append(valor)
                print('Pedido confirmado ! Cobrado por quilo //',qt_quilos,' peças // Lavagem a seco // Preço Final R$',valor)
            else:
                lista_valores.append(valor)
                print('Pedido confirmado ! Cobrado por quilo //',qt_quilos,' peças // SEM lavagem a seco Preço Final R$',valor)
        else:
            print('Escolha uma opção válida')

   
    if a < 4:
        print('----------------------------Próximo pedido------------------------------------------')
    else:
        print('------------------------------Resultado---------------------------------------------')


print('A quantidade de peças dos ultimos 5 pedidos foi:',peça)
print('A quantidade de quilo dos últimos 5 pedidos foi:',quilo)
print('A quantidade de lavagens a seco foi:',contador_seco)
print('A lista com os valores dos últimos 5 pedidos:',lista_valores)
print('A lavandeira ganhou nos últimos 5 pedidos: R$',sum(lista_valores))

input('Aperte Enter para fechar o programa')
quit()


