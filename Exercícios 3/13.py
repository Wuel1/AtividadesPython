input('Aperte Enter para iniciar o programa')
print('Olá ! Quais são os 5 alunos?')
alunos = []

for a in range(5):
    n = input()
    alunos.append(n)

tabela = []

for a in range(5):
    print('Digite as 4 notas do aluno',alunos[a],':')
    n1= float(input())
    n2= float(input())
    n3= float(input())
    n4= float(input())
    media = (n1 + n2 + n3 + n4)/4
    tabela.append(media)

aprovados = 0
reprovados = 0

for a in range(5):
    if tabela[a] >= 7:
        aprovados += 1
    else:
        reprovados += 1

print(aprovados,'Alunos foram aprovados')
print(reprovados,'Alunos foram reprovados')

for a in range(5):
    if tabela[a] >= 7:
        print('A média do aluno(a)',alunos[a],'é:',tabela[a],'Por isso está aprovado. Parabéns !')
    else:
        print('A média do aluno(a)',alunos[a],'é:',tabela[a],'Por isso está reprovado. :(')

input()
quit()
    
    
    

    
    
