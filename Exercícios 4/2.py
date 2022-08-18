#link formulário:
#https://docs.google.com/document/d/1w1ekrF3cQQpRR1w8Ji2fpEFIETuQbdF4VRLOG-lwAdU/edit

numero = 0
qtparespositivos = 0
print('Digite números inteiros:')
while numero <= 100:
    numero = int(input('-'))
    if numero % 2 == 0 and numero >= 0:
        qtparespositivos += 1
    else:
        continue
print('A quantidade de pares positivos informado foi:',qtparespositivos)
input('Aperte Enter para fechar o programa')
