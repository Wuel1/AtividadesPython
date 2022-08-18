def testeVogal (lista,carac):
    for i in lista:
        if i == carac:
            return True
    return False

lista = 'aeiou'

input('Aperte Enter para iniciar o programa')
print('Bem vindo ao testador de vogal')
print('Digite algum caractere para saber se é uma vogal')

x = 0
while x == 0:
    carac = input('-')
    carac = carac.lower()
        
    if testeVogal(lista,carac):
        print(testeVogal(lista,carac))
        print('Sim,(',carac,') é uma vogal')
    else:
        print(testeVogal(lista,carac))
        print('Não,(',carac,') não é uma vogal')

    a = int(input('Digite 1 caso queira continuar'))

    if a != 1:
        x += 1
    else:
        print('-------------------------------------------------')
        print('Digite outro caractere para saber se é uma vogal')


input('Aperte Enter para fechar o programa')


