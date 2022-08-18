def pedirlista (n):
    lista = []
    for a in range(n):
        x = float(input('-'))
        lista.append(x)
    return lista

input('Aperte Enter para iniciar o programa')
print('Digite 25 números:')

lista = pedirlista(25)
maior =  max(lista)

print('O maior número da lista é:',maior)
input('Aperte Enter para fechar o programa')
quit()
