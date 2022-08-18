input('Pressione Enter para iniciar o programa')
print('Qual seu nome?')
nome = input()
print('Olá,',nome,'Seja bem-vindo')
print('Qual a metade do diâmetro do circulo?(Em centimetros)')
r = float(input())
a = 3.14 * (r**2)
resultado = 'A área do circulo é:' + str(a) + ' cm²'
print(resultado)

input('Aperte Enter para encerrar o programa')
quit()
