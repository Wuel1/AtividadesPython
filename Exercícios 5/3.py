def m4 (op):
    if op % 4 == 0:
        return True
    return False

input('Aperte Enter para iniciar o programa')
print('Digite um número para saber se ele é múltiplo de 4')

while True:
    x = int(input('-'))
    if m4(x):
        print(m4(x))
        print('Esse número é múltiplo de 4')
    elif x == -1:
        break
    else:
        print(m4(x))
        print('Esse número não é múltiplo de 4')
        
    print('-------Digite outro número, ou um -1 para sair do programa---------')

input('Quit')
quit()
