def verifica_elementos_repetidos(matriz):
    x = False
    matrizUnica = []
    for w in matriz:
        for e in w:
            matrizUnica.append(e)
    for i in matrizUnica:
        if matrizUnica.count(i) > 1:
            x = True
    return x

matrizSemRepetição = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
matrizComRepetição = [[10, 20, 30], [10, 30, 60], [20, 80, 90]]

assert not verifica_elementos_repetidos(matrizSemRepetição)
assert verifica_elementos_repetidos(matrizComRepetição)

print(verifica_elementos_repetidos(matrizSemRepetição))
print(verifica_elementos_repetidos(matrizComRepetição))

