print('Olá, Digite 5 númeoros inteiros')
numeros = []
somador = 0
multiplicador = 1
for a in range(5):
    n = int(input('Digite o número:'))
    numeros.append(n)
    somador += n
    multiplicador *= n

print('A soma entre os números é:',somador)
print('A multiplicação entre os números é:',multiplicador)

input()
input('Aperte Enter para fechar o programa')
quit()
