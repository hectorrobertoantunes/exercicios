# Aluguel de carros

dias_alugados = int(input('Escreva o número de dias que você alugou o carro: '))
km_rodados = float(input('Escreva quantos quilômetro que você rodou no carro: '))
dia = 60
km_valor = 0.15
valor_total = (60*dias_alugados) + (km_rodados*km_valor)
print('O valor que você precisa pagar é de R$ {} reais'.format(valor_total))