input('Aperte Enter para iniciar o programa')
mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
mediap = []
soma = 0

for a in range(12):
    print('Digite a temperatura média do mês de',mes[a])
    temperatura = float(input('-'))
    soma += temperatura
    mediap.append(temperatura)

media =  soma/12

print(mes)
print(mediap)

print('A média da temperatura durante o ano foi de:',media,'º')

input()
input('Aperte Enter para fechar o programa')
quit()
