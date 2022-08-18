def ordena_palavras(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if len(lista[j]) < len(lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return

#Testando a função

lista = ['caju','uva','abacate','banana']

print('-Lista Original-')
print(lista)
ordena_palavras(lista)
print('-Lista Ordenada-')
assert lista == ['abacate','banana','caju','uva']
print(lista)
            
        
