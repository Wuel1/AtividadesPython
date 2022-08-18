numero = 0
somapares = 0
#n_pares = 0
lista_numero = []
print('Digite os números')
while numero != 100:
    numero = int(input('-'))
    if numero % 2 == 0 and numero != 100:
        somapares += numero
        #n_pares += 1
        lista_numero.append(numero)
    else:
        continue

n_pares = len(lista_numero)
media  = somapares/n_pares
print('A média dos números pares informados é:',media)
input('Aperte Enter para sair do programa')
