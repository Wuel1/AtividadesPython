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


print('Olá, Seja bem-vindo a venda de abadás do bloco Balança, mas não cai')
comissarios = 0
abadas = 0
lcomissarios = []
lquantidades = []
bonus = 0
while True:
    comissarios += 1
    print('Qual nome do comissário?')
    nome = input('-')
    lcomissarios.append(nome)
    print('Quantos abadás',nome,'vendeu?')
    x = int(input('-'))
    abadas += x
    lquantidades.append(x)

    print('Há mais comissários? SIM / NÃO')
    z = input('-')
    z = z.lower()

    if z == 'sim':
        continue
    elif z == 'não':
        break

print('----------------Resultados-----------------------')

valorpago = []

for i in lquantidades:
    y = calculaComissao(i)
    valorpago.append(y)
    
for i in range(len(lcomissarios)):
    print(lcomissarios[i],'Recebeu de comissão:',valorpago[i])
    print('-------------------------------------------------')

for i in lquantidades:
    if i >= 50:
        bonus += 1

print(bonus,'comissários receberam o bônus')
print('---------------------------------------------------')
print(sum(lquantidades),'abadás foram vendidos')
print('---------------------------------------------------')

a = obtemMenor(lquantidades)
for i in range(len(lquantidades)):
    if lquantidades[i] == a:
        print(lcomissarios[i],'Foi o que menos vendeu abadás, com um total de:',a,' abadás vendidos')

print('---------------------------------------------------')

a = obtemMaior(lquantidades)
for i in range(len(lquantidades)):
    if lquantidades[i] == a:
        print(lcomissarios[i],'Foi o que mais vendeu abadás, com um total de:',a,' abadás vendidos')

print('---------------------------------------------------')


input('- Aperte Enter para fechar o programa -')
quit()
        
    
    
    
