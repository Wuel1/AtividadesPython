## Chave = 3
## Apenas testando

def cifrar(entrada):
    saida = ''
    for i in entrada:
        for j in range(len(alfabeto)-1):
            if i == alfabeto[j]:
                saida += cifra[j]
    return saida


def decifrar(saida):
    retorno = ''
    for i in saida:
        for j in range(len(cifra)-1):
            if i == cifra[j]:
                retorno += alfabeto[j]
    return retorno

alfabeto = list("abcdefghijklmnopqrstuvwxyz")
cifra = list("defghijklmnopqrstuvwxyzabc")

print(alfabeto)

entrada = input().lower()

n = cifrar(entrada)
print('Codificado:', n)
d = decifrar(n)
print('Decodificado:', d)