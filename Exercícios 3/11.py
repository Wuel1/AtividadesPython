print('Digite a frase:')
frase = input()
vogais = 'aáAÁeéÉEiíIÍoóÓuúUÚ'
#espaço = ''
cvogais = 0
#cconsoantes = 0
#cespaço = 0

for a in frase:
    if a in vogais:
        cvogais += 1
    #else:
        #cconsoantes += 1

print('O número de vogais na frase é:',cvogais)
#print('O número de consoantes na frase é:',cconsoantes)
input()
quit()
     
        
