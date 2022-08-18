print('Digite o tamanho desejado da sequência desejada')
n = int(input('-'))

fib = [1,1]

for a in range(2,n):
    fib.append(fib[a-2] + fib[a-1])

print(fib)
