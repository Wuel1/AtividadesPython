print('Olá ! Esses são os números impares entre 0 e 50')
input('Aperte Enter para continuar')
numeros_impares = []
numeros_pares = []
numeros = list(range(1,51))
for a in numeros:
    if (a % 2 == 1):
        numeros_impares.append(a)
    else:
        numeros_pares.append(a)

print('Os números impares são:')
print(numeros_impares)
print('Os números pares são:')
print(numeros_pares)
input('Aperte Enter para fechar o programa')
quit()
