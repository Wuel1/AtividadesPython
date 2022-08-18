print('Bem vindo ao gerador de tabuada')
print('Digite o número entre 0 e 10 que você deseja saber a tabuada')
n = int(input())

if n <= 10:
    print('Entrada válida')    
else:
    print('O número tem que ser menor ou igual a 10')
    input()
    quit()

tabuada = list(range(11))
resultados = []

for a in tabuada:
    valor = n * a
    resultados.append(valor)

for b in range(11):
        print(n,'x', b,'=',n*b)

print('A lista com os resultados:')
print(resultados)
input()
input()
quit()
