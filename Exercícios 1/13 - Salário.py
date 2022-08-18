input('Aperte a teclar Enter para iniciar o programa')
print('Olá ! Qual é seu nome?')
nome = input()
print('Olá,',nome,' ! Seja bem-vindo')
_t = input('Você trabalha? sim / não : ')
if _t == 'não':
    input('Aperte Enter para fechar o programa')
    quit()
if _t == 'sim':
    print('Quanto você ganha por hora?')
    gh = float(input())
    print('Número de horas que você trabalha no mês:')
    hm = float(input())
    gm = gh * hm
    ir = (gm * 11) / 100
    inss = (gm * 8) / 100
    sind = (gm * 5) / 100
    sl = (gm - ir - inss - sind)

    print('O seu salário bruto é R$',gm)
    print('Você paga ao imposto de renda R$',ir)
    print('Você paga ao INSS R$',inss)
    print('Você paga ao sindicato R$',sind)
    print('O seu salário líquido é R$',sl)

    input('Aperte Enter para fechar o programa')
    quit()
