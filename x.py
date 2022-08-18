def fact (a):
    valor = 1
    for i in range(1,a+1):
        valor = i * (i+1)
        valor += valor
    return valor

x = fact(5)
print(x)
