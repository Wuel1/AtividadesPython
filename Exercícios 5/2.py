def calculaMaior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
print('Seja bem vindo')
while True:
    print('Digite dois números:')
    numero1 = float(input('1º:'))
    numero2 = float(input('2º:'))

    print(calculaMaior(numero1,numero2),'é o maior número')

    print('Você deseja continuar')
    print('1 para sim // 2 para não')
    x = 0
    while x == 0:
        a = float(input('-'))
        if a == 1:
            x += 1
        elif a == 2:
            break
        else:
            print('Escolha uma opção válida')
    if a == 1:
        continue
    break

print('Aperte Enter para sair do programa')
input()
    
