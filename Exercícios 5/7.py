import math

def estacionamento (auto,horas):
    if auto == 'carro' or auto != 'moto':
        if horas <= 5:
            return 3
        elif horas > 5:
            return 3 + (2*math.ceil((horas-5)))
        
    if auto == 'moto':
        if horas <= 5:
            return 1.50
        elif horas > 5:
            return 1.50 + math.ceil((horas-5))
        
print('Seja bem-vindo ao shopping legal')
while True:
    
    print('Informe se seu veículo é um carro, moto, ou outro automóvel:')
    auto = input('-')
    auto = auto.lower()
    print('Quantas horas você deixou o veículo estacionado?')
    horas = float(input('-'))
    print('Quantos minutos você deixou o veículo estacionado?')
    minutos = float(input('-'))

    minutos = minutos / 60

    horas += minutos

    valor = estacionamento(auto,horas)

    print('O valor a ser pago do estacionamento é:',valor,'Reais')

    print('Você deseja conferir outro valor? Sim / Não')
    
    x = input('-')
    x = x.lower()
    
    if x == 'sim':
       continue
    elif x == 'não':
       break
        
        
input('Aperte Enter para fechar o programa')
quit()
