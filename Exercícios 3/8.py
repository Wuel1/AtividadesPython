input('Aperte Enter para iniciar o programa')
print('Digite dois números')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
intervalo = list(range(n1 + 1,n2))

print('O intervalo entre esses dois números é:')
print(intervalo)

somador = 0
for a in intervalo:
    somador += a

print('A soma de todos esses números contidos nesse intervalo é:', somador)
input('Aperte ENTER para fechar')
quit()
