# Programa para ler 20 números e
# exibir a soma dos pares
cont = 1
soma = 0
print('Digite 20 números inteiros')
while (cont <= 20):
   numero = int (input('-'))
   if (numero % 2 == 0):
       soma += numero
       cont += 1
   else:
       cont += 1
print('A soma dos números pares informados é:',soma)




