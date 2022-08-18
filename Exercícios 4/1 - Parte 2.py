# Programa para ler 30 números e
# exibir a quantidade de positivos
cont = 1
qtdePositivos = 0
print('Digite 30 números inteiros')
while (cont <= 30):
    numero = int (input())
    if (numero >= 0):
        qtdePositivos += 1
        cont += 1
    else:
        cont += 1

print('A quantidade de números positivos é',qtdePositivos)
input('Aperte Enter para fechar o programa')
