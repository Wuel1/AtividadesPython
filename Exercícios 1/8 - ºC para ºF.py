input('Pressione alguma tecla para iniciar')
print('Olá ! Qual seu nome?')
nome = input()
print('Olá !',nome,'Seja bem-vindo!')

print('Qual a temperatura da sua cidade em ºCelcius?')
C = float(input())

F = (C * 1.8) + 32

resultado = 'A temperatura da sua cidade em ºFahrenheit é de ' + str(F)

print(resultado)

input('Aperte Enter para fechar o programa')
quit()
