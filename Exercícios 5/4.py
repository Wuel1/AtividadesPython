def tdiv (n1,n2):
    if n1 % n2 == 0:
        return True
    return False

input('Aperte Enter para iniciar o programa')
print('Digite dois números:')

while True:
    x = int(input('1º-'))
    y = int(input('2º-'))
    if tdiv(x,y):
        print(tdiv(x,y))
        print(y,'é divisor de',x)
    elif x == -1 or y == -1:
        break
    else:
        print(tdiv(x,y))
        print(y,'não é divisor de',x)

    print('Digite outros dois números, ou -1 para sair do programa')

input('Quit')
quit()
