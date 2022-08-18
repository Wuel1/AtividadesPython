def calculaComissao (a):
    if a <= 50:
        a1 = a*80
        return (a1*7)/100
    elif a > 50:
        a1 = a*80
        return ((a1*7)/100) + 70

def calculaBonus (a):
    if a <= 50:
        return 0
    elif a > 50:
        return 70

def obtemMenor (lista):
    if lista == []:
        return None
    else:
        return min(lista)

def obtemMaior (lista):
    if lista == []:
        return None
    else:
        return max(lista)

