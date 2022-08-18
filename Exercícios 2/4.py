input('Aperte Enter para iniciar o programa')
print('Digite um número:')
num = float(input())

impar = num%2 == 1
m_3 = num%3 == 0
d_102 = 102%num == 0

if impar == True:
    print(num,'é impar')
else:
        print(num,'é par')
        
input('Aperte Enter para continuar')

if m_3 == True:
    print(num,'é multiplo de 3')
else:
        print(num,'não é multiplo de 3')
        
input('Aperte Enter para continuar')

if d_102 == True:
    print(num,'é divisor de 102')
else:
        print(num,'não é divisor de 102')

input('Aperte Enter para fechar o programa')
quit()
    
