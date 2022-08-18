print('Digite 5 Números para calcular a soma e a média')
numeros = []
contador = 0
for a in range(5):
    n = float(input('Digite o número:'))
    contador += n
    numeros.append(n)

media = contador/5

print('Os números digitados foram:',numeros)
print('A soma é:',contador)
print('A média dos números digitados é:',media)

input()
quit()
