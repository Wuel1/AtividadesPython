print('Digite 4 notas para cálcular a média')

somador = 0
for a in range(4):
    notas = float(input('Digite:'))
    somador += notas

media = somador/4

print('A média é:', media)

if media >= 7:
    print('Parabéns ! Você passou ')
    input()
    quit()
elif media >= 3:
    print('Infelizmente você não passou, porém ainda pode fazer final')
    input()
    quit()
else:
    print('Infelizmente você reprovou')
    input()
    quit()
