alunos = []
for a in range(5):
    print('Olá, digite o nome do',a + 1,'aluno(a):')
    nome = input()
    alunos.append(nome)

idade = []
altura = []

for a in range(5):
    print(alunos[a],'digite sua idade:')
    ida = int(input('-'))
    print(alunos[a],'digite sua altura:')
    h = float(input('-'))
    idade.append(ida)
    altura.append(h)

print('As idades informadas na ordem inversa são:')
print(idade[::-1])
print('As alturas informadas na ordem inversa são:')
print(altura[::-1])
print('Os nomes informados na ordem inversa são:')
print(alunos[::-1])

input()
input('Aperte Enter para fechar o programa')
quit()
