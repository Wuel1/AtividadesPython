input('Aperte Enter para iniciar o programa')
print('Olá ! Seja bem vindo a 1 questão do mini teste 3')
print('Digite os 3 lados do triângulo')

lados = []

for a in range(3):
    l = float(input('-'))
    lados.append(l)

A = lados[0]
B = lados[1]
C = lados[2]

if A + B > C and B + C > A and A + C > B:
    print('Esses valores podem formar um triângulo')
    if A == B == C:
        print('O triângulo formado por esses valores é equilatero')
    elif A != B != C:
        print('O triângulo formado por esses valores é escaleno')
    else:
        print('O triângulo formado por esses valores é isósceles')
        
else:
   print('--- Esses valores NÃO podem formar um triângulo ---')

input()
input('Aperte Enter para iniciar o programa')
quit()


