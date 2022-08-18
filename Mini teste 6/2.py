def obtem_linhas_nulas(matriz):
    linhasNulas = 0
                 #[0,1,2,3]
    for i in range(len(matriz)):
        for j in range(len(matriz)-i -1):
            x = matriz[i][j] + matriz[i][j+1]
        if x == 0:
            linhasNulas += 1                       
                
    return linhasNulas


def obtem_colunas_nulas(matriz):
    colunasNulas = 0
                 #[0,1,2]
    for i in range(len(matriz)-1):
        for j in range(len(matriz)-1):
            x = matriz[i][j] + matriz[i+1][j]
        if x == 0:
            colunasNulas += 1                       
                
    return colunasNulas

matriz = [[1,0,2,3],[4,0,5,6],[0,0,0,0],[0,0,0,0]]

#assert 2 == obtem_linhas_nulas(matriz)
#assert 1 == obtem_colunas_nulas(matriz)

print(obtem_linhas_nulas(matriz))
print(obtem_colunas_nulas(matriz))


