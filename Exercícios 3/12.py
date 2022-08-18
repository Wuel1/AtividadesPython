print('Olá ! Digite 20 números inteiros')
numeros = []
par = []
impar = []

for a in range(20):
    n = int(input('Digite o números:'))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print('Os 20 números inteiros são:')
print(numeros)
print('Estes são os números pares:')
print(par)
print('Estes são os números impares:')
print(impar)

input()
quit()
