input('Aperte Enter para iniciar o programa')
print('Olá João !')
peso = float(input('João, quantos kg você trouxe hoje? '))
excesso = peso - 50
multa = excesso * 4
if peso == 50:
    print('João, o que você trouxe hoje é igual ao limite, por isso não pagará multa.')
    input('Aperte Enter para fechar o programa')
    quit()      
   
if peso < 50.0:
    print('João, o que você trouxe hoje está dentro do limite, e por isso não pagará multa.')
    input('Aperte Enter para fechar o programa')
    quit()

if peso > 50.0:
    print('João, o que você trouxe hoje ultrapassou o limite, e por isso você PAGARÁ multa.')
    input('Aperte Enter para saber mais detalhes')
    print('Você excedeu o limite em',excesso,'kg. e pagará uma multa no valor de R$',multa,'Reais.')
    input('Aperte Enter para fechar o programa')
    quit()
