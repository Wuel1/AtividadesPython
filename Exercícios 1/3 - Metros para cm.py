input('Pressione a tecla enter para iniciar')
print('Qual é seu nome?')
nome = input()
print('Olá,',nome,'Seja bem-vindo ao conversor de Metros para centimetros!')
print('Quantos metros?')
m = float(input())
c = (m * 100)

resultado = str(m) + ' metros são ' + str(c) + ' centimetros'

print(resultado)

input('Pressione alguma tecla para fechar')
quit()
