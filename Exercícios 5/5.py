def tdiv (n1,n2):
    if n1 % n2 == 0:
        return True
    return False

def m4 (op):
    if op % 4 == 0:
        return True
    return False

print('Aperte Enter para iniciar o programa')
print('Digite 10 números')
lista = []
listam4 = []
listad300 = []
mu4 = 0
d300 = 0

for a in range(10):
    n = int(input('-'))
    lista.append(n)

for a in lista:
    if m4(a):
        print('----------------------')
        print(a,'é múltiplo de 4')
        mu4 += 1
        listam4.append(a)
    if tdiv(300, a):
        print('----------------------')
        print(a,'é divisor de 300')
        d300 += 1
        listad300.append(a)

print('----------Resultado------------')

print('Os números informados foram:')
print(lista)
print('-------------------------------')
print('A lista com os múltiplos de 4:')
print(listam4)
print('-------------------------------')
print('A lista com divisores de 300:')
print(listad300)
print('-------------------------------')

input('Aperte Enter para fechar o programa')
quit()
    
