input('Olá, Aperte Enter para iniciar o programa')
print('Digite os valores:')
valor1 = float(input('1º:'))
valor2 = float(input('2º:'))
valor3 = float(input('3º:'))

a = valor1 > valor2 and valor1 > valor3
b = valor2 > valor1 and valor2 > valor3
c = valor3 > valor1 and valor3 > valor2

if a == True:
    print('O maior valor é:',valor1)
elif b == True:
    print('O maior valor é:',valor2)
elif c == True:
    print('O maior valor é:',valor3)
else:
    print('Os valores são iguais')

input('Aperte Enter para fechar o programa')
quit()
